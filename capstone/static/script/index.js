window.addEventListener("load",function() {
    document.getElementById("dropdown").addEventListener("change",function() {
        const target = this.value;
        if (target == '1'){
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("1text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("login").href = '/login_sql_inj';
        } else if (target == '2') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("2text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("login").href = '/login_sql_inj';
        } else if (target == '3') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("login").href = '/login_sql_inj';
        } else {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
	    document.getElementById("login").style.display = 'none';
        }
    });
});

document.getElementById("sql1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "gatesb'-- ";
});


document.getElementById("sql2").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "gatesb' or 1=1 UNION SELECT user, id, balance, password FROM accounts;#";
});
