/* /usr/env/node node */

function actualizarAfluenciaDiaria() {
    // Obtener el valor seleccionado del menú desplegable (ID del comedor)
    const idComedor = document.getElementById("comedor").value;

    // Realizar una solicitud AJAX para obtener la afluencia actualizada
    fetch(`/tablero_afluencia?comedor=${idComedor}`)
        .then(response => response.json())
        .then(data => {
            const afluenciaSpan = document.getElementById("afluencia-value");
            afluenciaSpan.textContent = data.afluencia_dia;
        })
        .catch(error => {
            console.error(error);
        });
}

// Llamar a la función para obtener la afluencia al cargar la página
actualizarAfluenciaDiaria();

// Establecer una repetición para actualizar la afluencia diariamente
setInterval(actualizarAfluenciaDiaria, 86400000); // 86400000 ms = 24 horas