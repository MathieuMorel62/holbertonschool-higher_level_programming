/* Script to retrieve and list the titles of all Star Wars movies using the API */

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  $.each(data.results, function(index, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
