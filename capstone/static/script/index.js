window.addEventListener("load",function() {
    document.getElementById("dropdown").addEventListener("change",function() {
        const target = this.value;
        if (target == '1'){
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("1text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/sql_inj.pdf';
	    document.getElementById("download").download = 'SQL_Injection_Writeup.pdf';
	    document.getElementById("login").href = '/login_sql_inj';
        } else if (target == '2') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("2text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/XSS.pdf';
	    document.getElementById("download").download = 'XSS_Writeup.pdf';
	    document.getElementById("login").href = '/login_xss';
        } else if (target == '3') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '';
	    document.getElementById("download").download = '';
	    document.getElementById("login").href = '/login';
        } else {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
	    document.getElementById("login").style.display = 'none';
	    document.getElementById("download").style.display = 'none';
	    document.getElementById("download").href = '';
	    document.getElementById("download").download = '';
        }
    });
});
