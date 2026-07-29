#!/usr/bin/env python3
"""Collect visibility/performance metrics for souravchandra.com.

Stdlib-only for Hermes cron. Writes human Markdown reports and raw JSONL records.
"""
from __future__ import annotations
import datetime as dt, json, os, re, subprocess, time, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

BASE='https://souravchandra.com'
REPO=Path(__file__).resolve().parents[1]
REPORT_DIR=REPO/'reports'/'visibility'
RAW_DIR=REPORT_DIR/'raw'
UA='Mozilla/5.0 (compatible; SouravVisibilityBot/1.0; +https://souravchandra.com/robots.txt)'
GSC_SITE_CANDIDATES=['sc-domain:souravchandra.com','https://souravchandra.com/']
PSI_URLS=[BASE+'/', BASE+'/blog/', BASE+'/blog/fractional-cto-dubai-uae-guide.html', BASE+'/blog/cto-as-a-service-dubai.html']
TRACKED_KEYWORDS=['fractional CTO Dubai','fractional CTO UAE','CTO as a service Dubai','AI MVP development','technical due diligence checklist','non-technical founder building an app','RAG vs fine-tuning for startups']

def fetch(url, timeout=30):
    req=urllib.request.Request(url, headers={'User-Agent':UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body=r.read().decode('utf-8','ignore')
            return r.status,{k.lower():v for k,v in r.headers.items()},body,None
    except urllib.error.HTTPError as e:
        return e.code,{k.lower():v for k,v in e.headers.items()},e.read().decode('utf-8','ignore'),str(e)
    except Exception as e:
        return None,{},'',str(e)

def sitemap_urls():
    s,_,body,_=fetch(BASE+'/sitemap.xml')
    if s!=200: return [BASE+'/']
    try:
        root=ET.fromstring(body); ns={'sm':'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls=[e.text or '' for e in root.findall('.//sm:url/sm:loc', ns)]
        return sorted({u for u in urls if u.startswith(BASE)}) or [BASE+'/']
    except Exception:
        return [BASE+'/']

def checks(body):
    low=body.lower(); head=low[:low.find('</head>')] if '</head>' in low else low[:9000]
    return {'title':'<title' in head,'description':'name="description"' in head or "name='description'" in head,'canonical':'rel="canonical"' in head or "rel='canonical'" in head,'jsonld':'application/ld+json' in low,'og':'property="og:' in head or "property='og:" in head,'noindex':'noindex' in head,'bytes':len(body.encode('utf-8'))}

def gcloud_token():
    for cmd in [['/home/hermes/google-cloud-sdk/bin/gcloud','auth','application-default','print-access-token'],['/home/hermes/google-cloud-sdk/bin/gcloud','auth','print-access-token']]:
        try:
            cp=subprocess.run(cmd,text=True,capture_output=True,timeout=20)
            if cp.returncode==0 and cp.stdout.strip(): return cp.stdout.strip()
        except Exception: pass
    return None

def api_json(url, token=None, method='GET', payload=None, timeout=45):
    data=None if payload is None else json.dumps(payload).encode()
    headers={'User-Agent':UA,'Accept':'application/json'}
    qp=os.environ.get('GOOGLE_CLOUD_QUOTA_PROJECT') or os.environ.get('GOOGLE_CLOUD_PROJECT')
    if not qp:
        adc=Path.home()/'.config'/'gcloud'/'application_default_credentials.json'
        try:
            qp=json.loads(adc.read_text(encoding='utf-8')).get('quota_project_id')
        except Exception:
            qp=None
    if qp and token and 'key=' not in url: headers['X-Goog-User-Project']=qp
    if token: headers['Authorization']='Bearer '+token
    if data: headers['Content-Type']='application/json'
    req=urllib.request.Request(url,headers=headers,method=method,data=data)
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r: return json.loads(r.read().decode('utf-8','ignore')),None
    except urllib.error.HTTPError as e:
        body=e.read().decode('utf-8','ignore')
        try: msg=json.loads(body).get('error',{}).get('message') or body[:300]
        except Exception: msg=body[:300]
        return None,f'HTTP {e.code}: {msg}'
    except Exception as e: return None,str(e)

def previous_gsc_blocker():
    """Preserve the most specific known Search Console blocker across auth gaps.

    In unattended cron, a local gcloud token can disappear after a prior run already
    proved that the Google account lacked access to the Search Console property.
    Reporting BLOCKED_AUTH after that is less useful than continuing to tell the
    owner to verify/add access for the site property.
    """
    search=REPORT_DIR/'search-visibility-daily.md'
    if search.exists() and 'BLOCKED_SITE_ACCESS' in search.read_text(encoding='utf-8'):
        return 'BLOCKED_SITE_ACCESS'
    raw=RAW_DIR/'visibility-metrics.jsonl'
    if raw.exists():
        for line in raw.read_text(encoding='utf-8').splitlines():
            try:
                if json.loads(line).get('gsc',{}).get('status')=='BLOCKED_SITE_ACCESS':
                    return 'BLOCKED_SITE_ACCESS'
            except Exception:
                continue
    return None

def collect_gsc():
    token=gcloud_token()
    if not token:
        prior=previous_gsc_blocker()
        if prior=='BLOCKED_SITE_ACCESS':
            return {'status':'BLOCKED_SITE_ACCESS','error':'Previous authenticated GSC call returned site-access/verification failure; no fresh token today, preserving the specific blocker.'}
        return {'status':'BLOCKED_AUTH','error':'No gcloud access token available'}
    end=dt.date.today()-dt.timedelta(days=1); start=end-dt.timedelta(days=6)
    payload={'startDate':start.isoformat(),'endDate':end.isoformat(),'dimensions':['query','page','country','device'],'rowLimit':50,'startRow':0}
    last=None
    for site in GSC_SITE_CANDIDATES:
        url='https://www.googleapis.com/webmasters/v3/sites/'+urllib.parse.quote(site,safe='')+'/searchAnalytics/query'
        data,err=api_json(url,token=token,method='POST',payload=payload)
        if data is not None:
            rows=data.get('rows',[]); totals={'clicks':0,'impressions':0,'ctr_weighted':0,'position_weighted':0}
            for r in rows:
                imp=float(r.get('impressions',0)); clicks=float(r.get('clicks',0))
                totals['clicks']+=clicks; totals['impressions']+=imp; totals['ctr_weighted']+=float(r.get('ctr',0))*imp; totals['position_weighted']+=float(r.get('position',0))*imp
            totals['ctr']=(totals['ctr_weighted']/totals['impressions']) if totals['impressions'] else 0
            totals['position']=(totals['position_weighted']/totals['impressions']) if totals['impressions'] else 0
            return {'status':'OK','site':site,'startDate':payload['startDate'],'endDate':payload['endDate'],'totals':totals,'rows':rows}
        last=err
    markers=('not a verified Search Console site','sufficient permission for site')
    status='BLOCKED_SITE_ACCESS' if last and any(m in last for m in markers) else ('BLOCKED_AUTH' if last and ('403' in last or 'Permission' in last or 'Insufficient' in last) else 'ERROR')
    return {'status':status,'error':last}

def collect_pagespeed():
    out=[]
    for url in PSI_URLS:
        params={'url':url,'strategy':'mobile','category':['performance','seo','accessibility']}
        key=os.environ.get('PAGESPEED_API_KEY') or os.environ.get('GOOGLE_PAGESPEED_API_KEY')
        if key: params['key']=key
        data,err=api_json('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?'+urllib.parse.urlencode(params,doseq=True),timeout=90)
        if data is None:
            t=time.perf_counter(); s,h,b,e=fetch(url,45); ms=round((time.perf_counter()-t)*1000)
            out.append({'url':url,'status':'SYNTHETIC','pagespeed_status':'BLOCKED_QUOTA' if err and ('Quota' in err or '429' in err) else 'ERROR','pagespeed_error':err,'http_status':s,'fetch_ms':ms,'bytes':len(b.encode('utf-8')) if b else 0,'cache_control':h.get('cache-control','')})
            continue
        cats=data.get('lighthouseResult',{}).get('categories',{}); audits=data.get('lighthouseResult',{}).get('audits',{})
        out.append({'url':url,'status':'OK','performance':round((cats.get('performance',{}).get('score') or 0)*100),'seo':round((cats.get('seo',{}).get('score') or 0)*100),'accessibility':round((cats.get('accessibility',{}).get('score') or 0)*100),'lcp':audits.get('largest-contentful-paint',{}).get('displayValue','n/a'),'cls':audits.get('cumulative-layout-shift',{}).get('displayValue','n/a'),'tbt':audits.get('total-blocking-time',{}).get('displayValue','n/a')})
    return out

def ensure(path,title,header):
    if not path.exists(): path.write_text(f'# {title}\n\n{header}\n',encoding='utf-8')

def replace_key(path,row):
    text=path.read_text(encoding='utf-8') if path.exists() else ''
    key=row.split('|')[1].strip(); lines=[]; done=False
    for line in text.splitlines():
        if line.startswith('|') and len(line.split('|'))>2 and line.split('|')[1].strip()==key:
            if not done: lines.append(row); done=True
            continue
        lines.append(line)
    if not done: lines.append(row)
    path.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

def main():
    REPORT_DIR.mkdir(parents=True,exist_ok=True); RAW_DIR.mkdir(parents=True,exist_ok=True); today=dt.date.today().isoformat()
    urls=sitemap_urls(); items=[]; ok=meta=0
    for u in urls:
        s,h,b,e=fetch(u); c=checks(b); m=s==200 and c['title'] and c['description'] and c['canonical'] and c['jsonld'] and not c['noindex']
        ok+=1 if s==200 else 0; meta+=1 if m else 0; items.append({'url':u,'status':s,'error':e,'metadata_ok':m,'checks':c})
    assets={p:{'status':fetch(BASE+p)[0],'ok':fetch(BASE+p)[0]==200} for p in ['/robots.txt','/sitemap.xml']}
    gsc=collect_gsc(); psi=collect_pagespeed(); home_s,home_h,_,home_e=fetch(BASE+'/')
    rec={'date':today,'base':BASE,'routes':{'total':len(urls),'ok':ok,'metadata_ok':meta,'items':items},'assets':assets,'homepage':{'status':home_s,'error':home_e,'cache_control':home_h.get('cache-control',''),'last_modified':home_h.get('last-modified','')},'gsc':gsc,'pagespeed':psi,'tracked_keywords':TRACKED_KEYWORDS}
    with (RAW_DIR/'visibility-metrics.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(rec,sort_keys=True)+'\n')
    search=REPORT_DIR/'search-visibility-daily.md'; ensure(search,'Search Visibility Daily Metrics','| Date UTC | GSC Status | Clicks | Impressions | CTR | Avg Position | Top Query | Top Page | Notes |\n|---|---|---:|---:|---:|---:|---|---|---|')
    if gsc.get('status')=='OK':
        rows=gsc.get('rows') or []; top=rows[0] if rows else {}; keys=top.get('keys') or ['n/a','n/a']; t=gsc['totals']
        row=f"| {today} | OK | {int(t['clicks'])} | {int(t['impressions'])} | {t['ctr']*100:.2f}% | {t['position']:.1f} | {keys[0]} | {keys[1] if len(keys)>1 else 'n/a'} | {gsc['startDate']}→{gsc['endDate']} via {gsc['site']} |"
    else: row=f"| {today} | {gsc.get('status')} |  |  |  |  |  |  | {str(gsc.get('error','')).replace('|','/')[:180]} |"
    replace_key(search,row)
    psf=REPORT_DIR/'pagespeed-weekly.md'; ensure(psf,'PageSpeed / UX Metrics','| Date UTC | URL | Status | Mobile Perf | LCP | CLS | TBT | SEO | Accessibility | Action |\n|---|---|---|---:|---|---:|---|---:|---:|---|')
    rows=[]
    for p in psi:
        short=p['url'].replace(BASE,'') or '/'
        if p.get('status')=='OK': action='Fix perf' if p['performance']<90 else 'Monitor'; rows.append(f"| {today} | {short} | OK | {p['performance']} | {p['lcp']} | {p['cls']} | {p['tbt']} | {p['seo']} | {p['accessibility']} | {action} |")
        else: rows.append(f"| {today} | {short} | {p.get('pagespeed_status','ERROR')}+SYNTHETIC |  | fetch {p.get('fetch_ms')}ms |  | bytes {p.get('bytes')} |  |  | Enable PageSpeed API quota; monitor synthetic fetch trend |")
    # replace all today rows for page speed
    old=psf.read_text(encoding='utf-8').splitlines(); kept=[l for l in old if not(l.startswith('|') and len(l.split('|'))>2 and l.split('|')[1].strip()==today)]
    psf.write_text('\n'.join(kept+rows).rstrip()+'\n',encoding='utf-8')
    actions=REPORT_DIR/'recurring-actions.md'; ensure(actions,'Recurring Growth Actions','| Date UTC | Trigger | Evidence | Action Taken | PR | Status | Follow-up Date |\n|---|---|---|---|---|---|---|')
    print(f"Sourav visibility metrics {today}\nRoutes: {ok}/{len(urls)} HTTP 200; metadata: {meta}/{len(urls)}\nAssets: robots={'OK' if assets['/robots.txt']['ok'] else 'FAIL'}, sitemap={'OK' if assets['/sitemap.xml']['ok'] else 'FAIL'}\nGSC: {gsc.get('status')}\nPageSpeed: "+', '.join([p['url'].replace(BASE,'')+('='+(str(p.get('performance')) if p.get('status')=='OK' else p.get('pagespeed_status','ERROR'))) for p in psi]))
    return 0
if __name__=='__main__': raise SystemExit(main())
