$(document).on('submit', '#signupForm', function(e){
    e.preventDefault();

    $.ajax({
      type: 'POST',
      url: '/signup',
      data: {
        name: $("#name").val(),
        email: $("#email").val(),
        password: $("#password").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(response){
        if (response.success){
            alert(response.message);
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }
      },
      error: function(response){
        alert(response.message);
      }
    })
})