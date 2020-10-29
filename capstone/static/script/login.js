var path = document.getElementById('refer').innerHTML;
var page = path.split("/");

if (page[page.length - 1] == "login_sql_inj"){
	document.getElementById('vulnerability').innerHTML = "SQL Injection";
} else if (page[page.length - 1] == "login_xss"){
	document.getElementById('vulnerability').innerHTML = "Cross Site Scripting";
} else{
	document.getElementById('vulnerability').innerHTML = page[page.length - 1];
}
