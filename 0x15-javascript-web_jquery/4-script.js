// toggles class of <header> on click

$(document).ready(function () {
    $("DIV#toggle_header").click(function () {
        $("header").toggleClass("red green");
    });
});
