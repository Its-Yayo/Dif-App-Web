/* /usr/env/node node */

document.getElementById("comedor").addEventListener("change", function() {
    const comedorName = this.value;
    console.log(`Comedor seleccionado: ${comedorName}`);

    // Realizar una solicitud AJAX para obtener la lista de productos del inventario
    fetch(`/inventario_lista?comedor=${comedorName}`)
        .then(response => response.json())
        .then(data => {
            if (data && !data.error) {
                const productosBody = document.getElementById("productos-body");
                productosBody.innerHTML = ""; // Limpia el contenido anterior

                data.productos.forEach(producto => {
                    const row = productosBody.insertRow();
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    const cell3 = row.insertCell(2);
                    const cell4 = row.insertCell(3);

                    cell1.textContent = producto.cantidad;
                    cell2.textContent = producto.descripcion;
                    cell3.textContent = producto.presentacion;
                    cell4.textContent = producto.unidadMedida;
                });
            } else {
                console.log("Error al obtener la lista de productos del inventario.");
                console.log(data.error);
            }
        })
        .catch(error => {
            console.error(error);
        });
});