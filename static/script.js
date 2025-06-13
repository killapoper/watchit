function openPlayer(title, description, poster, url) {
  document.getElementById('playerTitle').innerText = title;
  document.getElementById('playerDescription').innerText = description;
  document.getElementById('playerFrame').src = url;
  document.getElementById('playerModal').style.display = 'block';
}

function closePlayer() {
  document.getElementById('playerModal').style.display = 'none';
  document.getElementById('playerFrame').src = '';
}