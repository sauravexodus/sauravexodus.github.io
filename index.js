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

document.addEventListener('load', () => {
  const location = Intl.DateTimeFormat().resolvedOptions().timeZone?.includes("Dubai") ? "Dubai, UAE" : "Bangalore, India"
    document.querySelector('.location').innerHTML = location
})
    