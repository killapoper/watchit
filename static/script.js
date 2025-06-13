document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    const modal = document.querySelector('.modal');
    modal.classList.add('active');
  });
});

document.querySelector('.close-btn').addEventListener('click', () => {
  document.querySelector('.modal').classList.remove('active');
});
