function submitForm(event) {
	// Stop non ajax post
	event.preventDefault();	

	// Check for captcha
	if (hcaptcha.getResponse() == "") {
		alert("Please fill out the captcha")
		return
	}

	// Get field entries
	form = document.getElementById("form");
	var formData = new FormData(form);
	var data = Object.fromEntries(formData);

	// Send post request
	minAjax({
		url:"https://contact.ampolic.com/contact.php",
		type:"POST",
		data: data,
		success: function(response) {
			form.reset();
			hcaptcha.reset();
			document.getElementById("form-response").innerHTML = response;
		}
  	});
}
