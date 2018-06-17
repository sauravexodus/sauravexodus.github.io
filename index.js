$(document).ready(() => {
  const languagesKnown = [
    'Typescript',
    'iOS',
    'Android',
    'React',
    'Swift',
    'Functional Programming',
    'Architecture Patterns', 
    'Sketch',
    'Redux Observable',
    'Kotlin',
    'Continuos Integration',
    'Adobe Photoshop',
    'Adobe Illustrator',
    'Adobe After Effects',
    'Ruby',
    'Rbuy on Rails',
    'Express.js',
    'GraphQL'
    ];
  var currentIndex = 1;
  window.setInterval(() => {
    $('#language').text(languagesKnown[currentIndex]);
    if (currentIndex == languagesKnown.length - 1) {
      currentIndex = 0;
    } else {
      currentIndex++;
    }
  }, 3000);
})