document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const hamburgerMenu = document.getElementById("hamburgerMenu");
    const darkToggle = document.getElementById("darkModeToggle");
    const darkToggleMobile = document.getElementById("darkModeToggleMobile");

    // Immediately check localStorage for dark mode
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        if (darkToggle) darkToggle.checked = true;
        if (darkToggleMobile) darkToggleMobile.checked = true;
    }

    // Hamburger toggle
    hamburger?.addEventListener("click", (event) => {
        event.stopPropagation();
        hamburger.classList.toggle("active");
        hamburgerMenu.classList.toggle("active");
    });

    // Close hamburger menu when clicking outside
    document.addEventListener("click", (event) => {
        if (!hamburger.contains(event.target) && !hamburgerMenu.contains(event.target)) {
            hamburger.classList.remove("active");
            hamburgerMenu.classList.remove("active");
        }
    });

    // Dark mode toggle
    darkToggle?.addEventListener("change", () => {
        if (darkToggle.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
            if (darkToggleMobile) darkToggleMobile.checked = true;
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
            if (darkToggleMobile) darkToggleMobile.checked = false;
        }
    });

    darkToggleMobile?.addEventListener("change", () => {
        if (darkToggleMobile.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
            if (darkToggle) darkToggle.checked = true;
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
            if (darkToggle) darkToggle.checked = false;
        }
    });
});
