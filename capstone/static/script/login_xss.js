window.addEventListener("load",function() {
	if (document.getElementById('UsernameInput').value == "None"){
		document.getElementById('UsernameInput').value = "";
	}
});

document.getElementById("xss1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "?user='/><script>alert('This page is vulnerable to XSS!');</script>";
});

document.getElementById("xss3").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "><script>alert(':(');</script>";
	document.getElementById('PasswordInput').value = "aaAA22@@";
});
