document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-password-toggle]").forEach(function (button) {
        button.addEventListener("click", function () {
            var input = document.getElementById(button.dataset.passwordToggle);
            if (!input) return;
            var visible = input.type === "password";
            input.type = visible ? "text" : "password";
            button.textContent = visible ? "Hide" : "Show";
            button.setAttribute("aria-label", visible ? "Hide password" : "Show password");
        });
    });

    document.querySelectorAll("form[data-confirm]").forEach(function (form) {
        form.addEventListener("submit", function (event) {
            if (!window.confirm(form.dataset.confirm)) event.preventDefault();
        });
    });

    var menuToggle = document.querySelector("[data-menu-toggle]");
    var sidebar = document.getElementById("sidebar");
    if (menuToggle && sidebar) {
        menuToggle.addEventListener("click", function () {
            var isOpen = sidebar.classList.toggle("open");
            menuToggle.setAttribute("aria-expanded", String(isOpen));
        });
        document.addEventListener("click", function (event) {
            if (window.innerWidth <= 850 && sidebar.classList.contains("open") &&
                !sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
                sidebar.classList.remove("open");
                menuToggle.setAttribute("aria-expanded", "false");
            }
        });
    }

    var printButton = document.querySelector("[data-print]");
    if (printButton) printButton.addEventListener("click", function () { window.print(); });
});
