
// Function to set a cookie
function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
// Function to get a cookie
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Function to show the cookies consent pop-up if the user has not yet accepted the cookies
function showCookiesPopup() {
  if (!getCookie('cookiesAccepted')) {
    document.getElementById('cookiesPopup').style.display = 'block';
  } else {
    document.getElementById('cookiesPopup').style.display = 'none';
  }
}

// Function to accept the cookies and hide the cookies consent pop-up
function acceptCookies() {
  setCookie('cookiesAccepted', true, 365);
  document.getElementById('cookiesPopup').style.display = 'none';
}

// Function to reject the cookies and hide the cookies consent pop-up
function rejectCookies() {
  setCookie('cookiesAccepted', false, 365);
  document.getElementById('cookiesPopup').style.display = 'none';
}

// Show the cookies consent pop-up when the page is loaded
document.addEventListener('DOMContentLoaded', function() {
  showCookiesPopup();
});