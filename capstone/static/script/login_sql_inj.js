document.getElementById("sql1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "gatesb'-- ";
});


document.getElementById("sql2").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "gatesb' or 1=1 UNION SELECT user, id, balance, password FROM accounts;#";
});
