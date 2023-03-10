// Get the <select> element
const selectElement = document.querySelector('#lessonType');

// Get the 'lessonType' value from localStorage
const lessonType = localStorage.getItem('lessonType');


// Set the default value of the <select> element to the 'lessonType' value, if it exists
if (lessonType) {
  // Find the <option> element with the matching ID and set it as the default
  const defaultOption = document.querySelector(`#${lessonType}`);
  console.log("default Option is");
  console.log(defaultOption.value);
  if (defaultOption) {
    selectElement.value = defaultOption.value;
  }
}


// Add an event listener to the <select> element
selectElement.addEventListener('change', function(event) {
  // Store the selected value in localStorage
  localStorage.setItem('lessonType', event.target.value);
});
