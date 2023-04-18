/* Display translation of "hello" with jQuery */


$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
});
