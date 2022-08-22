const statsContainer = document.querySelector('.stats-container')
statsContainer.addEventListener('click', function(event) {
  if (statsContainer.classList.contains("collapsed")) {
    statsContainer.classList.replace("collapsed", "expanded")
  }
})

const close = document.querySelector('.stats-container .close')
close.addEventListener('click', function(event) {
  if (statsContainer.classList.contains("collapsed")) {
    statsContainer.classList.replace("collapsed", "expanded")
  } else {
    statsContainer.classList.replace("expanded", "collapsed")
    event.stopPropagation();
  }
})

fetch('http://ip-api.com/json')
  .then(res => res.json())
  .then(json => {
    const location = json.country === "India" ? "Bangalore, India" : "Dubai, UAE"
    document.querySelector('.location').innerHTML = location
  })