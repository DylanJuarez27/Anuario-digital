const images = [
  "https://mdbootstrap.com/img/new/fluid/city/028.jpg",
  "https://mdbootstrap.com/img/new/fluid/city/025.jpg",
  "https://mdbootstrap.com/img/new/fluid/city/020.jpg",
  "https://mdbootstrap.com/img/new/fluid/city/021.jpg",
  "https://mdbootstrap.com/img/new/fluid/city/023.jpg",
  "https://mdbootstrap.com/img/new/fluid/city/030.jpg9h"
];

let currentIndex = 0;

function changeBackground() {
  document.body.style.backgroundImage = `url(${images[currentIndex]})`;
  currentIndex = (currentIndex + 1) % images.length;
}


window.addEventListener("DOMContentLoaded", () => {
  changeBackground(); 
  setInterval(changeBackground, 5000); 
});