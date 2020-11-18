window.addEventListener("load",function() {
	var path = document.getElementById('attackToken').value;

	if (path == "1"){
		document.getElementById('vulnerability').innerHTML = "SQL Injection";
		document.getElementById('switchOn').href = "/login_sql_inj";
		document.getElementById("attackToken").value = "1";
		document.getElementById("sqlButtons").style.display = '';
		document.getElementById("sql1").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "gatesb'-- ";
		});
		document.getElementById("sql2").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "gatesb' or 1=1 UNION SELECT user, id, balance, password FROM accounts;#";
		});

	} else if (path == "2"){
		document.getElementById('vulnerability').innerHTML = "Cross Site Scripting";
		document.getElementById('switchOn').href = "/login_xss";
		document.getElementById("xssButtons").style.display = '';
		document.getElementById("attackToken").value = "2";
		document.getElementById("xss1").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "?user='/><script>alert('This page is vulnerable to XSS!');</script>";
		});
		document.getElementById("xss3").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "><script>alert(':(');</script>";
			document.getElementById('PasswordInput').value = "aaAA22@@";
		});
	} else if (path == "3"){
		document.getElementById('vulnerability').innerHTML = "Security Misconfiguration";
		document.getElementById('switchOn').href = "/login_misconfig";
		document.getElementById("misconfigButtons").style.display = '';
		document.getElementById("attackToken").value = "3";
		document.getElementById("misconfig1").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "admin";
			document.getElementById('PasswordInput').value = "admin";
		});
		document.getElementById("misconfig2").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "fakeUsername";
		});
	} else if (path == "4"){
		document.getElementById('vulnerability').innerHTML = "Broken Authentication";
		document.getElementById('switchOn').href = "/login_sessions";
		document.getElementById("sessionsButtons").style.display = '';
		document.getElementById("attackToken").value = "4";
		document.getElementById("sessions1").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "scottm";
			document.getElementById('PasswordInput').value = "DundlerMifflin123!";
		});
	} else if (path == "5"){
		document.getElementById('vulnerability').innerHTML = "Sensitive Data Exposure";
		document.getElementById('switchOn').href = "/login_exposure";
		document.getElementById("attackToken").value = "5";
		document.getElementById("exposureButtons").style.display = '';
		document.getElementById("sde1").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, id, balance, encrypted_password FROM accounts_md5;#";
		});
		document.getElementById("sde2").addEventListener("click", function(){
			document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, id, balance, encrypted_password FROM accounts_sha256;#";
		});
	} else{
		document.getElementById("unsafe").style.display = 'none';
	}
});

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("passwordbtn");
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal box
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  document.getElementById("msg").innerHTML = "";
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
	document.getElementById("msg").innerHTML = "";  
    modal.style.display = "none";
  }
}

document.getElementById("ResetPasswordButton").addEventListener("click", function(){
	document.getElementById("msg").innerHTML = "Password Reset Link Sent!";
});
