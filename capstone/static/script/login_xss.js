document.getElementById("xss1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "?user='/><script>alert('This page is vulnerable to XSS!');</script>";
});
