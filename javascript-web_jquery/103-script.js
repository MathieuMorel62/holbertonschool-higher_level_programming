/* Script that fetches and prints how to say “Hello” depending on the language*/

$(document).ready(function () {
  function translateHello() {
    const languageCode = $("#language_code").val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

    $.getJSON(`${url}${languageCode}`, function (data) {
        $("#hello").text(data.hello);
      }
    );
  }

  $("#btn_translate").click(translateHello);

  $("#language_code").keydown(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
