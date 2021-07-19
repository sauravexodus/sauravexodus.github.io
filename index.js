const statsContainer = document.querySelector('.stats-container')
statsContainer.addEventListener('click', function(event) {
  if (statsContainer.classList.contains("collapsed")) {
    statsContainer.classList.replace("collapsed", "expanded")
  }
})

const close = document.querySelector('.stats-container .close')
close.addEventListener('click', function(event) {
  statsContainer.classList.replace("expanded", "collapsed")
  event.stopPropagation();
})