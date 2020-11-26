$(function() {
    $('#submit').click(function() {
        var form_data = new FormData($('#upload')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadImg',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log(data);
		if (typeof(data) === 'string' || data instanceof String) {
			document.getElementById('postData').innerHTML = '<img id="rendered" src="" />';
			document.getElementById('rendered').src = "/static/files/" + data;
		}else{
			document.getElementById('postData').innerHTML = data;
		}
            },
        });
    });
});

document.getElementById("download").style.display = 'block';
document.getElementById("download").href = '/static/files/cheque.svg';
document.getElementById("download").download = 'cheque.svg';
