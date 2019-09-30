$(document).ready(function(){
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
    $('input#username, input#password, input#instructions').characterCounter();
    $('select').material_select();

// Close displayed flash message
    $('.close-btn').click(function() {
        $('#flashed-message').remove();
    });
})
