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
	} else{
		document.getElementById("unsafe").style.display = 'none';
	}
});

