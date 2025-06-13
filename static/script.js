document.addEventListener("DOMContentLoaded", () => {
    const movies = [
        {
            title: "Inception",
            img: "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg",
            description: "Погружение в сны. Фантастический триллер Нолана.",
            trailer: "https://www.youtube.com/watch?v=YoHD9XEInc0"
        },
        {
            title: "Interstellar",
            img: "https://image.tmdb.org/t/p/w500/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
            description: "Путешествие сквозь пространство и время.",
            trailer: "https://www.youtube.com/watch?v=zSWdZVtXT7E"
        },
        {
            title: "The Dark Knight",
            img: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
            description: "Легендарный Бэтмен с Джокером.",
            trailer: "https://www.youtube.com/watch?v=EXeTwQWrcwY"
        },
        {
            title: "Avatar",
            img: "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
            description: "Фантастика, покорившая планету.",
            trailer: "https://www.youtube.com/watch?v=5PSNL1qE6VY"
        },
        {
            title: "Dune",
            img: "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
            description: "Масштабная сага на песках Арракиса.",
            trailer: "https://www.youtube.com/watch?v=n9xhJrPXop4"
        }
        // Добавь ещё фильмы по шаблону
    ];

    const container = document.getElementById("movie-container");

    movies.forEach(movie => {
        const el = document.createElement("div");
        el.className = "movie";
        el.innerHTML = `
            <img src="${movie.img}" alt="${movie.title}">
            <div class="movie-description">
                <strong>${movie.title}</strong><br>
                ${movie.description}<br>
                <a href="${movie.trailer}" target="_blank" style="color:#1e90ff;">▶️ Смотреть трейлер</a>
            </div>
        `;
        container.appendChild(el);
    });
});