document.addEventListener("DOMContentLoaded", function () {
  const movieGrid = document.querySelector(".movie-grid");

  const movies = [
    { title: "Интерстеллар", poster: "https://upload.wikimedia.org/wikipedia/ru/b/bc/Interstellar_2014.jpg" },
    { title: "Дюна", poster: "https://upload.wikimedia.org/wikipedia/ru/2/20/Dune_2021.jpg" },
    { title: "Начало", poster: "https://upload.wikimedia.org/wikipedia/ru/d/d5/Inception2010.jpg" },
    { title: "Опенгеймер", poster: "https://upload.wikimedia.org/wikipedia/ru/b/bd/Oppenheimer_film_poster.jpg" },
    // Добавь свои
  ];

  movies.forEach(movie => {
    const card = document.createElement("div");
    card.className = "movie-card";

    card.innerHTML = `
      <img src="${movie.poster}" alt="${movie.title}">
      <div class="title">${movie.title}</div>
    `;

    movieGrid.appendChild(card);
  });

  // Поиск
  const searchInput = document.querySelector(".search-input");
  searchInput.addEventListener("input", function () {
    const value = this.value.toLowerCase();
    document.querySelectorAll(".movie-card").forEach(card => {
      const title = card.querySelector(".title").textContent.toLowerCase();
      card.style.display = title.includes(value) ? "block" : "none";
    });
  });
});