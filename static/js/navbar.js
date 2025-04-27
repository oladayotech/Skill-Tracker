document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const hamburgerMenu = document.getElementById("hamburgerMenu");
    const darkToggle = document.getElementById("darkModeToggle");

    // Hamburger toggle
    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        hamburgerMenu.classList.toggle("active");
    });

    // Dark mode toggle
    darkToggle.addEventListener("change", () => {
        if (darkToggle.checked) {
            document.body.classList.add("dark-mode");
        } else {
            document.body.classList.remove("dark-mode");
        }
    });
});
