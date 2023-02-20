$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const code = $('INPUT#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + code, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
