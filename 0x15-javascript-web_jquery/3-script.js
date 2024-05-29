// Adds the class 'red' to <header> on click

$(document).ready(function () {
    $("DIV#red_header").click(function () {
        $("header").addClass("red");
    });
});
