document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".carousel-item");
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");
    let currentIndex = 0;

    const updateCarousel = () => {
        items.forEach((item, index) => {
            item.classList.toggle("active", index === currentIndex);
        });
    };

    prev.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + items.length) % items.length;
        updateCarousel();
    });

    next.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % items.length;
        updateCarousel();
    });

    updateCarousel();
});
