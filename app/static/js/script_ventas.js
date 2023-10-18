/* /usr/env/node node */

function actualizarVentasTotales() {
    console.log("La funcion actualizarVentasTotales se ha ejecutado");
    const comedorId = document.getElementById("comedor").value;

    fetch(`/recaudaciones_ventas?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            const ventasSpan = document.getElementById("ventas-value");
            ventasSpan.textContent = data.recaudaciones_ventas;
        })
        .catch(error => {
            console.error(error);
        });
}

actualizarVentasTotales();

setInterval(actualizarVentasTotales, 10000); // Actualizar cada 10 segundos
