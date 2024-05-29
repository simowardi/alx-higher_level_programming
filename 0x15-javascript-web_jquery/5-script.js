// Adds an LI element to the list when user clicks div#add_item

$(document).ready(function () {
    $("DIV#add_item").click(function () {
        $("<li>").text("Item").appendTo("ul.my_list");
    });
});
