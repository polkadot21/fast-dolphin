// Define the Markdown text
const fullUrl =  backendUrl + "/" + version + "/" + "users/";
console.log("full url:");
console.log(fullUrl);
var markdownText = '# Вы вышли из аккаунта\n\n' +
                    'Пока, <username>! ' +
                    '👋🏽\n\n' +
                    'Вот ваши варианты:\n\n## ' +
                    '<a href="/login" target="_blank"> 📝 Войти</a>\n\n##' +
                    '<a href="/" target="_blank"> 🤗 Вернуться на главную</a>';

// Create a new converter object
var converter = new showdown.Converter();

// Convert the Markdown text to HTML
var htmlText = converter.makeHtml(markdownText);

// Get the access token from local storage
var accessToken = localStorage.getItem('access_token');

if (accessToken) {
  fetch(fullUrl, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + accessToken
    }
  })
  .then(response => {
    if (response.status === 401) {
      // Redirect to login page if the response status code is 401 (unauthorized)
      window.location.href = '/login';
    }
    return response.json();
  })
  .then(data => {
    // Get the user's first name and surname from the response data
    var firstName = data.Resources[0].FirstName;
    var surname = data.Resources[0].Surname;

    // Replace the <username> placeholder in the Markdown text with the user's name
    htmlText = htmlText.replace('<username>', firstName + ' ' + surname);

    // Set the inner HTML of the container div to the HTML text
    document.getElementById('markdown-container').innerHTML = htmlText;

    // Remove the access_token from local storage
    localStorage.removeItem('access_token');
  })
  .catch(error => {
    console.error('Error:', error);
  });
} else {
  window.location.href = '/login';
}
