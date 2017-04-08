$(document).ready(function(){

var csrftoken = getCookie('csrftoken');
  if (csrftoken == null) {
      csrftoken = $("[name='csrfmiddlewaretoken']").val();
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

      $('.imgbutton').click(function(e){
        $.get('/imgupload/',function(response){
            if(response != null){
                $('#lightbox_content').empty();
                $('#lightbox_content').html(response);
                $('#lightbox').css('display','inline');
            }
        })
    })

});

function closeModal() {
  document.getElementById('lightbox').style.display = "none";
  $('#lightbox_content').removeClass('lightbox_errorwidth').addClass('lightbox_width');
}
