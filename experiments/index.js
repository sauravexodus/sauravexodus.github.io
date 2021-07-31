const iframe = document.querySelector('.preview > iframe');

[...document.querySelectorAll('ul.experiment-list > li > a')].map(element => {
  element.addEventListener('click', () => {
    iframe.setAttribute('src', element.getAttribute('data-link'))
  })
})