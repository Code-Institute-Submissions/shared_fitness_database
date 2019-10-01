$(document).ready(function() {
    $(".button-collapse").sideNav();
    $('input#username, input#password, input#instructions').characterCounter();
    $('select').material_select();
})

// Close displayed flash message
$('.close-btn').click(function() {
    $('#flashed-message').remove();
});

// Fix created by CI to sort out the issue with the select elements not working as required
document.getElementsByClassName("matfix").addEventListener("click", function(e) {
    e.stopPropagation();
});

