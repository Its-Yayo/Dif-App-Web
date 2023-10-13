// Código para el boton del sidenav
document.addEventListener("DOMContentLoaded", function() {
    const toggleNavButton = document.getElementById("toggleNav");
    const sideNav = document.getElementById("sideNav");
    const body = document.body;

    // Agregar un evento al botón para abrir/cerrar el navbar
    toggleNavButton.addEventListener("click", function() {
        sideNav.classList.toggle("open");
        body.classList.toggle("side-nav-open");
    });

    // Agregar un evento al documento para cerrar el navbar si se hace clic fuera de él
    document.addEventListener("click", function(event) {
        if (!sideNav.contains(event.target) && event.target !== toggleNavButton) {
            sideNav.classList.remove("open");
            body.classList.remove("side-nav-open");
        }
    });

    // Evitar que el clic en el botón propague al documento y cierre inmediatamente el navbar
    toggleNavButton.addEventListener("click", function(event) {
        event.stopPropagation();
    });
});


