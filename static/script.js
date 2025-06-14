document.addEventListener("DOMContentLoaded", () => {
  const movieGrid = document.querySelector(".movie-grid");
  const searchInput = document.querySelector(".search-input");
  const loader = document.getElementById("loader");

function showLoader() {
  loader.style.display = "flex";
}

function hideLoader() {
  loader.style.display = "none";
}


async function searchMovies(query) {
  movieGrid.innerHTML = `<p style="text-align:center">Поиск «${query}»...</p>`;
  showLoader(); // ← Показываем индикатор

  try {
    const res = await fetch(`https://api-movies.github.io/kodik/search?title=${encodeURIComponent(query)}`);
    const data = await res.json();
    return data.results || [];
  } catch (err) {
    console.error("Ошибка при запросе:", err);
    return [];
  } finally {
    hideLoader(); // ← Скрываем индикатор
  }
}


  function renderMovies(movies) {
    movieGrid.innerHTML = "";
    if (movies.length === 0) {
      movieGrid.innerHTML = `<p style="text-align:center">Фильмы не найдены</p>`;
      return;
    }

    movies.forEach(movie => {
      const card = document.createElement("div");
      card.className = "movie-card";

      card.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}">
        <div class="title">${movie.title}</div>
      `;

      card.addEventListener("click", () => {
        openPlayer(movie.source);
      });

      movieGrid.appendChild(card);
    });
  }

  function openPlayer(source) {
    const win = window.open("", "_blank");
    win.document.write(`
      <html>
      <head>
        <title>Смотреть</title>
        <style>
          body { margin: 0; background: #000; }
          iframe { width: 100vw; height: 100vh; border: none; }
        </style>
      </head>
      <body>
        <iframe src="${source}" allowfullscreen></iframe>
      </body>
      </html>
    `);
  }

  searchInput.addEventListener("keypress", async (e) => {
    if (e.key === "Enter" && searchInput.value.trim()) {
      const results = await searchMovies(searchInput.value.trim());
      renderMovies(results);
    }
  });
});
