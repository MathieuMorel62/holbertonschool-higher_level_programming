/* Adding an item to a list using jQuery */

$('#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
