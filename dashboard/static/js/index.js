
// Eye icon toggle 
$(".toggle_password").click(function() {
    $(this).toggleClass("mdi-eye-outline mdi-eye-off-outline");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
        input.attr("type", "text");
    } else {
        input.attr("type", "password");
    }
});


// Login //
$("#login_form").on('submit', function (e) {
	e.preventDefault()
	var form_data = $(this).serialize()
	$.post("login", form_data, function (res) {
		if (res["res"] == "success") {
			$("#register_form").trigger("reset")
      		location.href = 'home';
		} else {
			Swal.fire({
				position: 'center',
				icon: 'error',
				title: res['msg'],
				showConfirmButton: false,
				timer: 5000
			})
		}
	})
	return false
})


// Register //
$("#register_form").on('submit', function (e) {
	e.preventDefault()
	var form_data = $(this).serialize()
	$.post("register", form_data, function (res) {
		if (res["res"] == "success") {
			$("#register_form").trigger("reset")
			Swal.fire({
				position: "center",
				icon: "success",
				title: res['msg'],
				showConfirmButton: false,
				timer: 5000
			})
      location.href = '/';

		} else {
			Swal.fire({
				position: 'center',
				icon: 'error',
				title: res['msg'],
				showConfirmButton: false,
				timer: 1500
			})
		}
	})
	return false
})

