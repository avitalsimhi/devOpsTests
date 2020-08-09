

# xhr = new XMLHttpRequest();
# // false as 3rd argument will forces synchronous processing
# xhr.open('POST', 'http://httpbin.org/post', false);
# xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
# xhr.send('login=test&password=test');
# alert(xhr.response);