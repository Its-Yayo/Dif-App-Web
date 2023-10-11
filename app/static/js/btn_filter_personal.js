// JavaScript

// Función para mostrar u ocultar elementos según la categoría seleccionada
function filtrarPorCategoria(categoria, contenedor) {
    const elementos = contenedor.querySelectorAll('.elemento'); // Reemplaza ".elemento" con la clase real de los elementos que deseas filtrar

    elementos.forEach(elemento => {
        const categoriaElemento = elemento.getAttribute('data-categoria');
        if (categoria === 'todos' || categoria === categoriaElemento) {
            elemento.style.display = 'block';
        } else {
            elemento.style.display = 'none';
        }
    });
}

// Agregar un controlador de eventos a los enlaces de filtro
document.querySelectorAll('.filtro-link').forEach(enlace => {
    enlace.addEventListener('click', function (e) {
        e.preventDefault();
        const categoria = this.getAttribute('data-categoria');
        const contenedor = this.closest('.item-1, .item-2'); // Busca el contenedor padre (empleados o voluntarios)

        // Filtra los elementos en el contenedor
        filtrarPorCategoria(categoria, contenedor);
    });
});
