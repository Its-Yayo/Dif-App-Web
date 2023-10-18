/* /usr/env/node node */

document.getElementById("comedor").addEventListener("change", function() {
    const comedorId = this.value;
    console.log(`Comedor seleccionado: ${comedorId}`);

    // Realizar una solicitud AJAX para obtener el administrador
    fetch(`/personal_lista?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            if (data && !data.error) {
                const listaAdminDiv = document.getElementById("lista-administradores");
                listaAdminDiv.innerHTML = ""; // Limpia el contenido anterior

                const table = document.createElement("table");
                const row = table.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);

                cell1.textContent = data.nombre;
                cell2.textContent = data.curp;

                listaAdminDiv.appendChild(table);
            } else {
                console.log("Error al obtener el administrador.");
                console.log(data.error);
            }
        })
        .catch(error => {
            console.error(error);
        });
});