function ValidationEvent() {
var name = document.getElementById("name").value;
var email = document.getElementById("email").value;
var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;

if (name != '' && email != '') {
if (email.match(emailReg)) {
return true;
} else {
alert("Invalid email address...!!!");
return false;
}
} else {
alert("All fields are required.....!");
return false;
}
}
