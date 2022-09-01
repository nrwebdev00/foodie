const carsouleImages = document.getElementsByClassName('carsoule-image');
const carsouleCaption = document.getElementsByClassName('carsoule-caption');
const carsouleLeftArrow = document.getElementById('carsoule-arrow-left');
const carsouleRightArrow = document.getElementById('carsoule-arrow-right');

let activeSlide = 0;
carsouleImages[0].classList.remove('image-display-none');
carsouleCaption[0].classList.remove('image-display-none');

carsouleLeftArrow.addEventListener('click', ()=>{
    if(activeSlide > 0){
        carsouleImages[activeSlide].classList.add('image-display-none');
        carsouleCaption[activeSlide].classList.add('image-display-none');
        activeSlide = activeSlide - 1;
        carsouleImages[activeSlide].classList.remove('image-display-none');
        carsouleCaption[activeSlide].classList.remove('image-display-none');
        console.log(activeSlide)
    }
})

carsouleRightArrow.addEventListener('click', ()=>{
    if(activeSlide < carsouleImages.length - 1){
        carsouleImages[activeSlide].classList.add('image-display-none');
        carsouleCaption[activeSlide].classList.add('image-display-none');
        activeSlide = activeSlide + 1;
        carsouleImages[activeSlide].classList.remove('image-display-none');
        carsouleCaption[activeSlide].classList.remove('image-display-none');
        console.log(activeSlide)
    }
})



console.log(activeSlide)