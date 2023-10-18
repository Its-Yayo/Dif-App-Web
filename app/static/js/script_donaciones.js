/* /usr/env/node node */

function actualizarDonacionesTotales() {
    console.log("La funcion actualizarDonacionesTotales se ha ejecutado");
    const comedorId = document.getElementById("comedor").value;

    fetch(`/recaudaciones_donaciones?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            const donacionesSpan = document.getElementById("donaciones-value");
            donacionesSpan.textContent = data.recaudaciones_donaciones;
        })
        .catch(error => {
            console.error(error);
        });
}

actualizarDonacionesTotales();

setInterval(actualizarDonacionesTotales, 10000); // Actualizar cada 10 segundos