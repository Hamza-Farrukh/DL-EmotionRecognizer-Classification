$(document).on('submit', '#loginForm', function(e){
    e.preventDefault();

    $.ajax({
      type: 'POST',
      url: '/',
      data: {
        email: $("#email").val(),
        password: $("#password").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(response){
        if (response.success){
            alert(response.message);
            window.location.href = '/home'
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