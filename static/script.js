function openPlayer(title, description, poster, url) {
  document.getElementById('playerFrame').src = url;
  document.getElementById('playerTitle').innerText = title;
  document.getElementById('playerDescription').innerText = description;
  document.getElementById('playerModal').style.display = 'flex';
}

function closePlayer() {
  document.getElementById('playerFrame').src = '';
  document.getElementById('playerModal').style.display = 'none';
}

function filterMovies() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const cards = document.querySelectorAll('.movie-card');
  cards.forEach(card => {
    const title = card.innerText.toLowerCase();
    card.style.display = title.includes(query) ? 'block' : 'none';
  });
}

function filterCategory(category) {
  const cards = document.querySelectorAll('.movie-card');
  cards.forEach(card => {
    if (category === 'all') {
      card.style.display = 'block';
    } else {
      card.style.display = card.classList.contains(category) ? 'block' : 'none';
    }
  });
}