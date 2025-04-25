// static/js/darkmode.js

// document.addEventListener('DOMContentLoaded', () => {
//     const toggle = document.getElementById('darkModeToggle');
//     const body = document.querySelector('.body');

//     if (localStorage.getItem('theme') === 'light') {
//         body.classList.add('light-mode');
//         toggle.checked = true;
//     }

//     toggle.addEventListener('change', function () {
//         if (this.checked) {
//             body.classList.add('light-mode');
//             localStorage.setItem('theme', 'light');
//         } else {
//             body.classList.remove('light-mode');
//             localStorage.setItem('theme', 'dark');
//         }
//     });
// });

function toggleMenu(element) {
    element.classList.toggle("active");
    document.getElementById("hamburgerMenu").classList.toggle("active");
}

// Optional: Add dark mode toggle behavior
const darkToggle = document.getElementById("darkModeToggle");
darkToggle.addEventListener("change", () => {
    document.body.classList.toggle("dark-mode");
});