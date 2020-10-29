var path = document.getElementById('refer').innerHTML;
var page = path.split("/");

if (page[page.length - 1] == "login_sql_inj"){
	document.getElementById('vulnerability').innerHTML = "SQL Injection";
	document.getElementById("sqlButtons").style.display = '';
	document.getElementById("sql1").addEventListener("click", function(){
		document.getElementById('UsernameInput').value = "gatesb'-- ";
	});
	document.getElementById("sql2").addEventListener("click", function(){
		document.getElementById('UsernameInput').value = "gatesb' or 1=1 UNION SELECT user, id, balance, password FROM accounts;#";
	});

} else if (page[page.length - 1] == "login_xss"){
	document.getElementById('vulnerability').innerHTML = "Cross Site Scripting";
	document.getElementById("xssButtons").style.display = '';
	document.getElementById("xss1").addEventListener("click", function(){
		document.getElementById('UsernameInput').value = "?user='/><script>alert('This page is vulnerable to XSS!');</script>";
	});
	document.getElementById("xss3").addEventListener("click", function(){
		document.getElementById('UsernameInput').value = "><script>alert(':(');</script>";
		document.getElementById('PasswordInput').value = "aaAA22@@";
	});
} else{
	document.getElementById("unsafe").style.display = 'none';
}


