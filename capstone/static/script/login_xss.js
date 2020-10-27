document.getElementById("xss1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = " '/><script>alert('XSS!');</script>";
});

