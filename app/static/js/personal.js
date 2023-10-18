/* /usr/env/node node */

document.getElementById("comedor").addEventListener("change", function() {
    const comedorId = this.value;
    console.log(`Comedor seleccionado: ${comedorId}`);

    // Realizar una solicitud AJAX para obtener los datos del administrador
    fetch(`/personal_lista?comedor=${comedorId}`)
        .then(response => response.json())
        .then(data => {
            if (data && data.personal_lista) {
                const listaAdminDiv = document.getElementById("lista-administradores");
                // Limpia el contenido anterior
                listaAdminDiv.innerHTML = "";

                // Muestra el nombre y el CURP del administrador
                const nombreElement = document.createElement("p");
                nombreElement.textContent = `Nombre: ${data.personal_lista.nombre}`;
                const curpElement = document.createElement("p");
                curpElement.textContent = `CURP: ${data.personal_lista.curp}`;

                listaAdminDiv.appendChild(nombreElement);
                listaAdminDiv.appendChild(curpElement);
            } else {
                console.log("Los datos recibidos no contienen personal_lista o son undefined.");
            }
        })
        .catch(error => {
            console.error(error);
        });
});