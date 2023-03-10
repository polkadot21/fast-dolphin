// Define the Markdown text
var markdownText = '### Вы успешно отправили заявку!\n\n' +
                    'Спасибо, <username>! ' +
                    '👋🏽\n\n' +
                    'Вы можете:\n\n#### ' +
                    '<a href="/new-customer-request" target="_blank"> 📝 Отправить еще одну заявку</a>\n\n####' +
                    '<a href="/" target="_blank"> 🤗 Вернуться на главную</a>';

// Create a new converter object
var converter = new showdown.Converter();

// Retrieve the firstName value from local storage
var firstName = localStorage.getItem('firstName');
if (!firstName) {
  firstName = 'добрый человек';
}

// Convert the Markdown text to HTML and replace the <username> placeholder with the user's name
var htmlText = converter.makeHtml(markdownText.replace('<username>', firstName));

// Set the inner HTML of the container div to the HTML text
document.getElementById('markdown-container').innerHTML = htmlText;
