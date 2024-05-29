// Updates text color of <header> to red when user clicks on DIV#red_header tag

document.readyState(function () {
    $('DIV#red_header').click(function () {
      $('header'.css('color', '#FF0000'));
    });
  });
