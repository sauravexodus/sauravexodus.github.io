document.querySelector('.stats-container').addEventListener('click', function(event) {
  const eventTarget = event.target;
  eventTarget.classList.replace("collapsed", "expanded")
})