const burger = document.getElementById('burger');
const navbarCollapse = document.getElementById('navbarCollapse');

burger.addEventListener('click', () => {
    navbarCollapse.classList.toggle('active');
});