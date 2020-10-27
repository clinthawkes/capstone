document.getElementById("xss1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "?user='/><script>alert('XSS!');</script>";
});

