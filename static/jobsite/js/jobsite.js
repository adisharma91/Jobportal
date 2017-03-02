//jobsite.js
$(document).ready(function(){
/*	$('#submitbtn').on('click',function(e){
		var userval = $('input[name="username"]').val();
		var userpass = $('input[name="password"]').val();

		if (userval == "")
		{
			e.preventDefault();
			$('.userempty').before('<span class="pull-right">username empty</span>');
		}
	});
*/

$('#myform').validationEngine({autoHidePrompt:true});
$("#submitbtn").validationEngine('validate');

});