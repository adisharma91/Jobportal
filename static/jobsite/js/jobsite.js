//jobsite.js
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


$('.form').validationEngine({autoHidePrompt:true, scroll: false});

$("#submitbtn").validationEngine('validate');
$("#signupbtn").validationEngine('validate');

$.get("/all_jobs_list/", function(result){

        for(i=0;i<=result.length;i++){
            availableTags.push('"'+result[i]+'"');
            }
});

$.get("/all_jobs_list/", function(result){

        for(i=0;i<=result.length;i++){
            availableTags.push('"'+result[i]+'"');
            }
});

var availableTags = [];
$( "#tags" ).autocomplete({
  source: availableTags
});

$('.regis').on('input',function(){
  $('.glyphicon').closest('span').remove();
  var username = $("input[name='username']").val();
 // alert(username);
      $.ajax({
            type:"POST",
            url: "/check_user_exists_or_not/",
            data: {
                   'username': username,
                  }

            }).done(function(response){
                if (response == 'Already_used') {
                    $('#id_username').parent('div').removeClass('has-feedback has-success');
                    $('#id_username').parent('div').addClass('has-feedback has-error');
                    $('#id_username').after('<span class="glyphicon glyphicon-remove form-control-feedback pad6" aria-hidden="true"></span>');
                }
                else{
                    $('#id_username').parent('div').removeClass('has-feedback has-error ');
                    $('#id_username').parent('div').addClass('has-feedback has-success ');
                    $('#id_username').after('<span class="glyphicon glyphicon-ok form-control-feedback pad6" aria-hidden="true"></span>');
                }
              });

  });


});
