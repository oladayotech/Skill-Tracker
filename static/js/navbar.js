document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const hamburgerMenu = document.getElementById("hamburgerMenu");
    const darkToggle = document.getElementById("darkModeToggle");

    // Toggle Hamburger Menu
    hamburger?.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        hamburgerMenu.classList.toggle("active");
    });

    // Toggle Dark Mode
    darkToggle?.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode", darkToggle.checked);
    });
});
