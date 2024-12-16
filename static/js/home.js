
document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll(".carousel img");
    const next = document.querySelector(".next");
    const prev = document.querySelector(".prev");
    let index = 0;

    const showImage = (i) => {
        images.forEach((img, idx) => img.classList.toggle("active", idx === i));
    };

    next.addEventListener("click", () => {
        index = (index + 1) % images.length;
        showImage(index);
    });

    prev.addEventListener("click", () => {
        index = (index - 1 + images.length) % images.length;
        showImage(index);
    });

    showImage(index);
});

// Button Interactivity
const buttons = document.querySelectorAll('.btn-buy');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        alert('¡Producto añadido al carrito!');
    });
});
