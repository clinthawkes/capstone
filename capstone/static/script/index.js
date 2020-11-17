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
	    document.getElementById("login").href = '/login_sql_inj?attackToken=1';
        } else if (target == '2') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("2text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/XSS.pdf';
	    document.getElementById("download").download = 'XSS_Writeup.pdf';
	    document.getElementById("login").href = '/login_xss?attackToken=2';
        } else if (target == '3') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/security_misconfig.pdf';
	    document.getElementById("download").download = 'Security_Misconfig_Writeup.pdf';
	    document.getElementById("login").href = '/login_misconfig?attackToken=3';
        } else if (target == '4') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("4text").style.display = 'block';
            document.getElementById("5text").style.display = 'none';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/broken_authentication.pdf';
	    document.getElementById("download").download = 'Broken_Authentication.pdf';
	    document.getElementById("login").href = '/login_sessions?attackToken=4';
        } else if (target == '5') {
            document.getElementById("1text").style.display = 'none';
            document.getElementById("2text").style.display = 'none';
            document.getElementById("3text").style.display = 'none';
            document.getElementById("4text").style.display = 'none';
            document.getElementById("5text").style.display = 'block';
	    document.getElementById("login").style.display = 'block';
	    document.getElementById("download").style.display = 'block';
	    document.getElementById("download").href = '/static/files/.pdf';
	    document.getElementById("download").download = '.pdf';
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
