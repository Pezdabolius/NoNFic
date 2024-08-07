// navbar

const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if(scrollY >= 180){
        navbar.classList.add('bg');
    } else{
        navbar.classList.remove('bg');
    }
})

// user icon popup

let userIcon = document.querySelector('.user-icon');
let userPopupIcon = document.querySelector('.user-icon-popup');

userIcon.addEventListener('click', () => userPopupIcon.classList.toggle('active'))

$('add_cart').submit(function (e) {
    e.preventDefault();
    $.ajax({
        type: $(this).attr('method'),
        url: '{% url \'add_cart\' %}',
        data: $(this).serialize(),
        success: function (response) {
            console.log(response);
        }
    });
});