let currentIndex = 0;

function showSlide(index) {

    const slides = document.querySelectorAll('.img-carousel-item');
    const descriptions = document.querySelectorAll('.description');
    if (index >= slides.length) currentIndex = 0;
    if (index < 0) currentIndex = slides.length - 1;
    const offset = -currentIndex * 100;
    document.querySelector('.img-carousel').style.transform = `translateX(${offset}%)`;

    slides.forEach((slide, i) => {
        if (i === currentIndex) {
            slide.classList.add('active');
            descriptions[i].classList.add('active');
        } else {
            slide.classList.remove('active');
            descriptions[i].classList.remove('active');
        }
    });

}

function nextSlide() {
    currentIndex++;
    showSlide(currentIndex);
}

function prevSlide() {
    currentIndex--;
    showSlide(currentIndex);
}

document.addEventListener('DOMContentLoaded', () => {
    const descriptions = document.querySelectorAll('.description');

    descriptions.forEach((description, i) => {
        description.addEventListener('click', () => {
            currentIndex = i;
            console.log(currentIndex)
            showSlide(currentIndex)
        })
    })
    showSlide(currentIndex);
});