$(document).ready(function() {
    $(".button-collapse").sideNav();
    $('input#username, input#password, input#instructions').characterCounter();
    $('select').material_select();
});

// Close displayed flash message
$('.close-btn').click(function() {
    $('#flashed-message').remove();
});

// Fix created by CI to sort out the issue with the select elements not working as required
// When clicked on, they were originally having a pop-in/pop-out effect and had to click on the select box a couple of
// times to get the dropdown options to stay in place, this fix solves that
document.getElementById("matfix1").addEventListener("click", function(e) {
    e.stopPropagation();
});
document.getElementById("matfix2").addEventListener("click", function(e) {
    e.stopPropagation();
});
document.getElementById("matfix3").addEventListener("click", function(e) {
    e.stopPropagation();
});
document.getElementById("matfix4").addEventListener("click", function(e) {
    e.stopPropagation();
});
document.getElementById("matfix5").addEventListener("click", function(e) {
    e.stopPropagation();
});
