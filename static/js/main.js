const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


setTimeout(function(){
    $('#message').fadeOut('slow');
},2000);


document.getElementById("loginForm").reset();
  
// ===================show/hide password-login screen==================

function showPassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }