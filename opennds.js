function senddata(){
	document.getElementById("submitBtn").disabled = true;
	document.getElementById("loader").classList.add("active");
	const form = document.getElementById("form");
	form.method = "get";
	form.action = "/opennds_preauth/"; 
	form.submit();
}
