/* /usr/env/node node */

function actualizarRecaudacionDiaria() {
    console.log("La funcion actualizarRecaudacionDiaria se ha ejecutado");
    const comedorId = document.getElementById("comedor").value;

    fetch(`/tablero_recaudacion?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            const recaudacionSpan = document.getElementById("recaudacion-value");
            recaudacionSpan.textContent = `$${data.recaudacion_dia.toFixed(2)}`;
        })
        .catch(error => {
            console.error(error);
        });
}

actualizarRecaudacionDiaria();

setInterval(actualizarRecaudacionDiaria, 86400000); // 86400000 ms = 24 horas