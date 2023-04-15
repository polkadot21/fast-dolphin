const backendUrl = "{{ env.BACKEND_URL }}"
const version = " {{ env.VERSION }}".trim()
const fullUrl =  backendUrl + "/" + version + "/" + "auth" + "/" + "access_token/";
const loginForm = document.querySelector('#login-form');
const usernameInput = document.querySelector('#username');
const passwordInput = document.querySelector('#password');
loginForm.addEventListener('submit', async (event) => {
  event.preventDefault(); // prevent form from submitting normally

  // make POST request to obtain access token
  console.log('Sending POST request...');
  const response = await fetch(fullUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      grant_type: '',
      username: usernameInput.value,
      password: passwordInput.value,
      scope: '',
      client_id: '',
      client_secret: ''
    })
  });

  // handle response based on status code
  console.log('Received response:', response.status);
  if (response.status === 200) {
    // extract access token from response
    const data = await response.json();
    const accessToken = data.access_token;
    console.log('Access token:', accessToken);

    // store access token in local storage
    localStorage.setItem('access_token', accessToken);

    // redirect to account page
    console.log('Redirecting to account page...');
    window.location.href = '/account';
  } else if (response.status === 401 || response.status === 404) {
    // display error message
    console.log('Incorrect username or password');
    alert('Incorrect username or password');
  } else {
    // display generic error message
    console.log('Failed to log in');
    alert('Failed to log in');
  }
});
