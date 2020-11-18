document.getElementById("sessions1").addEventListener("click", function(){
	document.getElementById('UsernameInput').value = "scottm";
	document.getElementById('PasswordInput').value = "DundlerMifflin123!";
});

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("passwordbtn");
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal box
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function open_in_new_window(id, new_page_title, features) {
    var new_window;

    if(features !== undefined && features !== '') {
    new_window = window.open('', '_blank', features);
    }
    else {
        new_window = window.open('', '_blank');
    }

    var html_contents = document.getElementById(id);
    if(html_contents !== null) {
	new_window.document.write('<!doctype html><html><head><title>' +
		new_page_title + '</title><meta charset="UTF-8" /><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"></head><body>' + html_contents.innerHTML + '</body></html>');
    }
}
