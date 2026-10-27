fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list_movies = document.querySelector('#list_movies');
    data.results.forEach(movie => {
      const list_item = document.createElement('li');
      list_item.textContent = movie.title;
      list_movies.appendChild(list_item);
    });
  });
