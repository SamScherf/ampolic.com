

function submitForm() {
	// Get data from form
   	var form = document.getElementById('form');
	var formData = new FormData(form);
	var data = Object.fromEntries(formData);

	// Send post request
	minAjax({
		url:"https://contact.ampolic.com/contact.php",
		type:"POST",
		data: data,
		success: function(){
			form.reset();
		}
  	});

	// Rest form temporarily
	form.reset();
}
