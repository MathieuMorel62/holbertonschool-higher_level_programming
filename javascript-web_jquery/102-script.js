/* Translation of 'Hello' according to language with jQuery and an external API */

$(document).ready(function() {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  
    $.get(`${url}?lang=${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
