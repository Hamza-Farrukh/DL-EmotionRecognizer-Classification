$(document).on('submit', '#imageForm', function(e){
    e.preventDefault();

    var form = new FormData(this);
    form.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
    
    $('#result').text("Processing...");
    var imageUrl = URL.createObjectURL(form.get("imageFile"));
    $('#image').attr('src', imageUrl);
    $('#imageURL').attr("href", imageUrl);

    $.ajax({
        type: 'POST',
        url: '/home',
        data: form,
        contentType: false,
        processData: false,
        success: function(response){
          if (response.success){
            $('#result').text(response.message);
          }
          else{
              $('#result').text("Error");
          }
        },
        error: function(response){
          $('#result').text("Error");
        }
    });
});
