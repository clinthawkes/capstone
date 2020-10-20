window.addEventListener("load",function() {
    document.getElementById("dropdown").addEventListener("change",function() {
        const target = this.value;
        if (target == '1'){
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("1text").style.display = 'block';
	    document.getElementById("login").href = "/login_sql_inj";
        } else if (target == '2') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("2text").style.display = 'block';
        } else if (target == '3') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'block';
        } else {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
        }
    });
});
