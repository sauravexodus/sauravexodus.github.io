#!/usr/bin/env python3
"""Score souravchandra.com visibility metrics against expected outcomes."""
from __future__ import annotations
import datetime as dt, json, os, re
from pathlib import Path
from typing import Any
REPO=Path(__file__).resolve().parents[1]; REPORT_DIR=REPO/'reports'/'visibility'; RAW=REPORT_DIR/'raw'/'visibility-metrics.jsonl'; EXPECTED=REPORT_DIR/'expected-outcomes.md'; SCORE=REPORT_DIR/'benchmark-scorecard.md'; BASE='https://souravchandra.com'
def num(s):
    s=str(s).strip().replace(',','')
    if s.lower() in {'','n/a','tbd'}: return None
    if s.endswith('%'): s=s[:-1]
    try: return float(s)
    except Exception: return None
def targets():
    out={}
    if not EXPECTED.exists(): return out
    for line in EXPECTED.read_text().splitlines():
        if not line.startswith('|') or 'Metric ID' in line or '---' in line: continue
        p=[x.strip() for x in line.strip('|').split('|')]
        if len(p)<9: continue
        h,mid,metric,base,tgt,stretch,dir,why,cad=p[:9]; days=int(re.sub(r'\D','',h) or '30')
        out.setdefault(mid,[]).append({'horizon':h,'days':days,'metric':metric,'target':num(tgt),'target_raw':tgt,'stretch':num(stretch),'stretch_raw':stretch,'direction':dir})
    for v in out.values(): v.sort(key=lambda r:r['days'])
    return out
def latest():
    if not RAW.exists(): return {}
    rec={}
    for line in RAW.read_text().splitlines():
        try: rec=json.loads(line)
        except Exception: pass
    return rec
def active(ts,mid,age=0):
    rows=ts.get(mid,[])
    if not rows: return None
    for r in rows:
        if age<=r['days']: return r
    return rows[-1]
def pct(a,b): return 0.0 if not b else float(a)/float(b)*100
def fmt(v,unit=''):
    if v is None: return 'n/a'
    if unit=='%': return f'{v:.1f}%'
    return str(int(round(v))) if abs(v-round(v))<.001 else f'{v:.2f}'
def cell(x): return str(x).replace('|','/').replace('\n',' ')[:200]
def is_brand_or_person_name_query(query):
    """Exclude Sourav-name variants and misrouted person-name queries.

    The scorecard's non-brand metric is meant to measure topical discovery. GSC
    currently surfaces misspellings such as ``saurabh chandra`` and unrelated
    names such as ``rishab chandra``; counting those as commercial non-brand
    discovery overstates progress.
    """
    normalized=re.sub(r'\s+',' ',str(query).strip().lower())
    if re.search(r'\b(?:sourav|saurav|saurabh)\b',normalized): return True
    return bool(re.fullmatch(r"[a-z][a-z .'-]{1,40} chandra",normalized))
def ai_rates():
    p=REPORT_DIR/'ai-visibility-weekly.md'
    if not p.exists(): return None,None,'No AI/GEO run recorded yet'
    rows=[]
    for line in p.read_text().splitlines():
        if not line.startswith('|') or '---' in line or 'Date' in line or 'Week' in line:
            continue
        cells=[cell.strip() for cell in line.strip('|').split('|')]
        if len(cells)>=5:
            rows.append((cells[3],cells[4]))
    if not rows: return None,None,'No AI/GEO run recorded yet'
    window=rows[:40]
    scored=[]
    for mention,citation in window:
        mention_state=mention.strip().lower(); citation_state=citation.strip().lower()
        if 'indeterminate' in mention_state or 'not scored' in mention_state or 'indeterminate' in citation_state or 'not scored' in citation_state:
            continue
        if not (mention_state.startswith(('yes','no')) and citation_state.startswith(('yes','no'))):
            continue
        scored.append((mention_state.startswith('yes'),citation_state.startswith('yes')))
    excluded=len(window)-len(scored)
    if not scored:
        return None,None,f'No determinate AI/GEO rows; {excluded} indeterminate excluded from newest {len(window)} rows'
    note=f'Scored {len(scored)} determinate rows; {excluded} indeterminate excluded from newest {len(window)} rows'
    return pct(sum(m for m,_ in scored),len(scored)),pct(sum(c for _,c in scored),len(scored)),note
def current(rec):
    out={}; g=rec.get('gsc',{}); t=g.get('totals',{}) if isinstance(g,dict) else {}
    if g.get('status')=='OK':
        out['gsc_impressions_7d']=(float(t.get('impressions',0) or 0),'',f"{g.get('startDate')}→{g.get('endDate')}"); out['gsc_clicks_7d']=(float(t.get('clicks',0) or 0),'',f"{g.get('startDate')}→{g.get('endDate')}"); out['gsc_ctr']=(float(t.get('ctr',0) or 0)*100,'%','Weighted by impressions'); pos=float(t.get('position',0) or 0); out['gsc_avg_position']=(pos if pos else None,'','No rank yet' if not pos else 'Weighted by impressions')
        qs={((r.get('keys') or [''])[0]) for r in g.get('rows',[]) if (r.get('keys') or [''])[0] and not is_brand_or_person_name_query((r.get('keys') or [''])[0])}
        out['nonbrand_query_count']=(float(len(qs)),'','Excludes Sourav/name-navigation variants from sampled GSC rows')
    else:
        for m in ['gsc_impressions_7d','gsc_clicks_7d','gsc_ctr','gsc_avg_position','nonbrand_query_count']: out[m]=(None,'',g.get('status','MISSING'))
    r=rec.get('routes',{}); total=float(r.get('total',0) or 0); out['technical_route_coverage']=(pct(r.get('ok',0),total),'%',f"{r.get('ok',0)}/{int(total)} routes HTTP 200"); out['metadata_coverage']=(pct(r.get('metadata_ok',0),total),'%',f"{r.get('metadata_ok',0)}/{int(total)} routes metadata OK")
    all_ps=rec.get('pagespeed',[])
    ps=[p for p in all_ps if p.get('status')=='OK']
    home=next((p for p in all_ps if p.get('url')==BASE+'/'), {})
    if home.get('status')=='OK' and home.get('performance') is not None:
        out['pagespeed_mobile_home']=(float(home['performance']),'','OK')
    elif home:
        page_status=home.get('pagespeed_status','ERROR')
        sample_status=home.get('status','UNKNOWN')
        evidence=page_status if page_status==sample_status else f'{page_status}+{sample_status}'
        out['pagespeed_mobile_home']=(None,'',evidence)
    else:
        out['pagespeed_mobile_home']=(None,'','Homepage PageSpeed missing')
    out['pagespeed_seo']=(min(float(p.get('seo',0) or 0) for p in ps),'','Minimum across tracked URLs') if ps else (None,'','PageSpeed not OK')
    out['pagespeed_accessibility']=(min(float(p.get('accessibility',0) or 0) for p in ps),'','Minimum across tracked URLs') if ps else (None,'','PageSpeed not OK')
    men,cit,note=ai_rates(); out['ai_mention_rate']=(men,'%',note); out['ai_citation_rate']=(cit,'%',note)
    out['serp_top20_coverage']=(None,'%','Competitor/SERP scan not yet recorded'); out['serp_top10_coverage']=(None,'%','Competitor/SERP scan not yet recorded'); out['source_gap_closure']=(None,'','Trend/source-gap action tracker not yet recorded')
    return out
def status(value,t):
    if t is None: return 'No target','Add expected outcome'
    if value is None: return 'Blocked','Need source data before benchmarking'
    tgt=t['target']; st=t['stretch']; d=t['direction']
    if tgt is None: return 'No target','Set numeric target'
    if d=='>=':
        if st is not None and value>=st: return 'Stretch','Protect and compound'
        if value>=tgt: return 'On track','Monitor'
        if value>=.8*tgt: return 'Watch','Nudge with targeted optimization'
        return 'Behind','Prioritize growth action'
    if d=='<=':
        if st is not None and value<=st: return 'Stretch','Protect and compound'
        if value<=tgt: return 'On track','Monitor'
        if value<=1.2*tgt: return 'Watch','Nudge with targeted optimization'
        return 'Behind','Prioritize growth action'
    return 'No target','Unsupported direction'
def report_date() -> dt.date:
    raw=os.environ.get('SOURAV_VISIBILITY_REPORT_DATE')
    return dt.date.fromisoformat(raw) if raw else dt.date.today()


def main():
    REPORT_DIR.mkdir(parents=True,exist_ok=True); rec=latest()
    if not rec: print('No metrics found'); return 2
    today=report_date().isoformat(); ts=targets(); cur=current(rec)
    mids=['gsc_impressions_7d','gsc_clicks_7d','gsc_ctr','gsc_avg_position','nonbrand_query_count','technical_route_coverage','metadata_coverage','pagespeed_mobile_home','pagespeed_seo','pagespeed_accessibility','ai_mention_rate','ai_citation_rate','serp_top20_coverage','serp_top10_coverage','source_gap_closure']
    rows=[]; counts={}
    for mid in mids:
        t=active(ts,mid); val,unit,evid=cur.get(mid,(None,'','Missing metric')); st,act=status(val,t); counts[st]=counts.get(st,0)+1; tgt=t['target'] if t else None; delta='n/a'
        if val is not None and tgt is not None: delta=fmt((val-tgt) if t['direction']=='>=' else (tgt-val),unit)
        rows.append(f"| {today} | {cell(t.get('horizon','n/a') if t else 'n/a')} | {mid} | {cell(t.get('metric',mid) if t else mid)} | {fmt(val,unit)} | {cell(t.get('target_raw','n/a') if t else 'n/a')} | {cell(t.get('stretch_raw','n/a') if t else 'n/a')} | {st} | {delta} | {cell(evid)} | {cell(act)} |")
    header='| Date UTC | Horizon | Metric ID | Metric | Current | Target | Stretch | Status | Delta | Evidence | Action |\n|---|---|---|---|---:|---:|---:|---|---:|---|---|'
    if not SCORE.exists(): SCORE.write_text('# Visibility Benchmark Scorecard\n\n'+header+'\n')
    kept=[l for l in SCORE.read_text().splitlines() if not(l.startswith('|') and len(l.split('|'))>2 and l.split('|')[1].strip()==today)]
    SCORE.write_text('\n'.join(kept+rows).rstrip()+'\n')
    print('Sourav benchmark scorecard '+today+': '+', '.join(f'{k}: {v}' for k,v in sorted(counts.items())))
    return 0
if __name__=='__main__': raise SystemExit(main())
