$(function () {
  $('DIV#red_header').click(function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
    } else {
      $('header').addClass('red');
    }
  });
});
