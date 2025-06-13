window.onload = () => {
  // Анимация карточек
  document.querySelectorAll('.card').forEach((c,i)=> {
    setTimeout(()=> {
      c.style.opacity=1; c.style.transform='translateY(0)';
    }, 150*i);
  });
};

function openFilm(id) {
  window.location = `/film/${id}`;
}
