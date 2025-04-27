document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const hamburgerMenu = document.getElementById("hamburgerMenu");
    const darkToggle = document.getElementById("darkModeToggle");

    // Immediately check localStorage for dark mode before anything
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        darkToggle.checked = true;
    }

    // Hamburger Toggle
    hamburger?.addEventListener("click", (event) => {
        event.stopPropagation(); // Prevent click from reaching document
        hamburger.classList.toggle("active");
        hamburgerMenu.classList.toggle("active");
    });

    // Close menu when clicking outside
    document.addEventListener("click", (event) => {
        if (!hamburger.contains(event.target) && !hamburgerMenu.contains(event.target)) {
            hamburger.classList.remove("active");
            hamburgerMenu.classList.remove("active");
        }
    });

    // Dark Mode Toggle
    darkToggle?.addEventListener("change", () => {
        if (darkToggle.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
        }
    });
});
