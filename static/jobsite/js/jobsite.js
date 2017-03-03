//jobsite.js
$(document).ready(function(){

$('#myform').validationEngine({autoHidePrompt:true});

$("#submitbtn").validationEngine('validate');

    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
$( "#tags" ).autocomplete({
  source: availableTags
});

$('.regis').keyup(function(){
  var username = $("input[name='username']").val();
 // alert(username);
      $.ajax({
            type:"POST",
            url: "/check_user_exists_or_not/",
            data: {
                   'username': username,
                  }

            }).done(function(response){
                  alert(response);
                if (response == 'True') {
                    alert(response);
                }
              });

  });

});
