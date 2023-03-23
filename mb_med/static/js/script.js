let burger = document.querySelector('.bars'),
    list = document.querySelector('.line'),
    navMenu = document.querySelector('.nav__menu');
    
burger.addEventListener('click', function(e) {
    e.preventDefault();
    burger.classList.toggle('active');
    list.classList.toggle('active');
    navMenu.classList.toggle('active');
})