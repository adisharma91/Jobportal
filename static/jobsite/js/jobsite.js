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

  $('.applybtn').click(function(e){
        e.preventDefault();
        $(this).html('Applied').attr('disabled',true);
        var action = $(this).data('href');
        $.post(action,$('#applyfrm').serialize(), function(response){
            if(response.success == 'true'){
                window.location = window.location
            }
        })
  })

});
