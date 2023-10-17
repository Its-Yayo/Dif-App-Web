/* /usr/env/node node */

function actualizarAfluenciaDiaria() {
    console.log("La funcion actualizarAfluenciaDiaria se ha ejecutado");
    const comedorId = document.getElementById("comedor").value;

    // Realizar una solicitud AJAX para obtener la afluencia actualizada
    fetch(`/tablero_afluencia?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            const afluenciaSpan = document.getElementById("afluencia-value");
            afluenciaSpan.textContent = data.afluencia_dia; // Debes usar el mismo nombre que estás pasando desde Flask en el template
        })
        .catch(error => {
            console.error(error);
        });
}

actualizarAfluenciaDiaria();

setInterval(actualizarAfluenciaDiaria, 86400000); // 86400000 ms = 24 horas