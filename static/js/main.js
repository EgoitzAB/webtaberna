/* Funcionalidad de apertura y cierre del navbar, con cierre si hay click en pantalla */

document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const closeMenu = document.getElementById("closeMenu");
    const menuOverlay = document.getElementById("menuOverlay");
    const menu = document.getElementById("menu");

    function toggleMenu() {
        menuOverlay.classList.toggle("active");
    }

    function closeMenuOnOutsideClick(event) {
        // Verifica si el clic ocurrió en el overlay pero no dentro del menú
        if (!menu.contains(event.target) && event.target !== menuToggle) {
            menuOverlay.classList.remove("active");
        }
    }

    menuToggle.addEventListener("click", toggleMenu);
    closeMenu.addEventListener("click", toggleMenu);
    menuOverlay.addEventListener("click", closeMenuOnOutsideClick);

    // Asegurarse de que el clic dentro del menú no cierre el menú
    menu.addEventListener("click", function(event) {
        event.stopPropagation(); // Evita que el clic dentro del menú cierre el menú
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.responsive-img');
    const contentBlocks = document.querySelectorAll('.content-block');

    function checkScroll() {
        const windowHeight = window.innerHeight;
        const scrollPosition = window.scrollY + (windowHeight / 2); // Poner el punto de activación en el centro de la pantalla

        images.forEach((img) => {
            const imgPosition = img.getBoundingClientRect().top + window.scrollY;

            // Activar cuando la posición superior de la imagen está cerca del centro de la pantalla
            if (scrollPosition > imgPosition) {
                img.classList.add('image-visible');
            }
        });

        contentBlocks.forEach((block) => {
            const blockPosition = block.getBoundingClientRect().top + window.scrollY;

            // Activar cuando la posición superior del bloque está cerca del centro de la pantalla
            if (scrollPosition > blockPosition) {
                block.classList.add('image-visible');
            }
        });
    }

    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Verifica al cargar la página
});

/* Funcionalidad Swiper para el carrousel */
document.addEventListener('DOMContentLoaded', function() {
    var swiper = new Swiper('.swiper-container', {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
            rotate: 30,
            stretch: 0,
            depth: 0,
            modifier: 1.5,
            slideShadows: true,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
});
