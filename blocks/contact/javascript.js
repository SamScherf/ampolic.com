hcaptcha_div = document.getElementById("h-captcha");

function loadCap() {

	// Check if h-captcha is already loaded
	if (!hcaptcha_div.hasChildNodes()) {
		// Load hcpatcha and log
		var widgetID = hcaptcha.render('h-captcha', { sitekey: 'd827d0bd-2dc5-4981-9784-b837691433b8'});
		console.log('hCaptcha is ready.');
	}
};


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
		url:"https://contact.ampolic.com/contact.php?UID=mA7jKe",
		type:"POST",
		data: data,
		success: function(response) {
			form.reset();
			hcaptcha.reset();
			document.getElementById("form-response").innerHTML = response;
		}
  	});
}
