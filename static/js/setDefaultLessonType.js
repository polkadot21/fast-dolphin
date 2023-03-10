// Get the <a> element
const oneTimeAWeekTraining = document.querySelector('#oneTimeAWeekTraining');
const twoTimesAWeekTraining = document.querySelector('#twoTimesAWeekTraining');
const personalTraining = document.querySelector('#personalTraining');

oneTimeAWeekTraining.addEventListener('click', function(event) {
  event.preventDefault(); // prevent the default behavior of the <a> tag

  // Store the lessonType value in local storage
  localStorage.setItem('lessonType', 'oneTimeAWeekTraining');

  // Redirect the user to the URL specified in the <a> tag
  window.location.href = oneTimeAWeekTraining.href;

});


twoTimesAWeekTraining.addEventListener('click', function(event) {
        event.preventDefault(); // prevent the default behavior of the <a> tag

        // Store the lessonType value in local storage
        localStorage.setItem('lessonType', 'twoTimesAWeekTraining');

        // Redirect the user to the URL specified in the <a> tag
        window.location.href = twoTimesAWeekTraining.href;
    }
);

personalTraining.addEventListener('click', function(event) {
        event.preventDefault(); // prevent the default behavior of the <a> tag

        // Store the lessonType value in local storage
        localStorage.setItem('lessonType', 'personalTraining');

        // Redirect the user to the URL specified in the <a> tag
        window.location.href = personalTraining.href;
    }
);
