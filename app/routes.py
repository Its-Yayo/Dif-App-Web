#!/usr/bin/python3

from typing import Any

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug import Response
import mariadb


main = Blueprint('main', __name__, template_folder='app/templates')

@main.route("/")
def main() -> str:
    return render_template("layout.html")

@main.route("/iniciar_sesion", methods=['GET', 'POST'])
def iniciar_sesion() -> Response | Any:
    if request.method == 'POST':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_Login', request.form['usuario'], request.form['contraseña'])
        usuario_final = cur.fetchone()

        if usuario_final:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('tablero'))
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'error')

    return login.html

@main.route("/cerrar_sesion", methods=['GET'])
def cerrar_sesion() -> Response:
    ...


@main.route("/tablero", methods=['GET'])
def tablero() -> None:
    render_template('tablero.html')

@main.route("/tablero/afluencia/<string:idComedor>", methods=['GET'])
def tablero_afluencia(idComedor: int) -> Response:
    ...

@main.route("/tablero/recaudacion", methods=['GET'])
def tablero_recaudacion() -> Response:
    ...

@main.route("/tablero/afluencia_año", methods=['GET'])
def tablero_afluencia_year() -> Response:
    ...

@main.route("/tablero/afluencia_comedores", methods=['GET'])
def tablero_comedores() -> Response:
    ...

@main.route("/afluencia", methods=['GET'])
def afluencia() -> None:
    ...

@main.route("/afluencia/<idComedor>/<condicion>", methods=['POST', 'GET'])
def afluencia_registros(idComedor: int, condicion: str) -> Response:
    ...

@main.route("/afluencia/inscritos/<idComedor>", methods=['GET'])
def afluencia_inscritos(idComedor: int) -> Response:
    ...

@main.route("/afluencia/predicciones/idComedor>", methods=['GET'])
def afluencia_predicciones(idComedor: int) -> Response:
    ...

@main.route("/recaudaciones", methods=['GET'])
def recaudaciones() -> None:
    ...

@main.route("/recaudaciones/<idComedor>/<condicion>", methods=['POST', 'GET'])
def recaudaciones_registros(idComedor: int, condicion: str) -> Response:
    ...

@main.route("/recaudaciones/donaciones/<idComedor>", methods=['GET'])
def recaudaciones_donaciones(idComedor: int) -> Response:
    ...

@main.route("/recaudaciones/ventas/<idComedor>", methods=['GET'])
def recaudaciones_ventas(idComedor: int) -> Response:
    ...

@main.route("/recaudaciones/lista_donaciones/", methods=['GET'])
def recaudaciones_lista_donaciones() -> Response:
    ...

@main.route("/recaudaciones/lista_ventas/", methods=['GET'])
def recaudaciones_lista_ventas() -> Response:
    ...

@main.route("/personal", methods=['GET'])
def personal() -> None:
    ...

@main.route("/personal/lista_personal/<idComedor>", methods=['GET'])
def personal_lista(idComedor: int) -> Response:
    ...

@main.route("/personal/agregar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_agregar(idComedor: int) -> Response:
    ...

@main.route("/personal/eliminar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_eliminar(idComedor: int) -> Response:
    ...

@main.route("/personal/modificar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_modificar(idComedor: int) -> Response:
    ...

@main.route("/invetario", methods=['GET'])
def inventario() -> None:
    ...

@main.route("/inventario/lista_inventario/<idComedor>", methods=['GET'])
def inventario_lista(idComedor: int) -> Response:
    ...

@main.route("/inventario/agregar_inventario/<idComedor>", methods=['POST', 'GET'])
def inventario_agregar(idComedor: int) -> Response:
    ...

@main.route("/inventario/eliminar_inventario/<idComedor>", methods=['POST', 'GET'])
def inventario_eliminar(idComedor: int) -> Response:
    ...

@main.route("/informe_costos", methods=['GET'])
def informe_costos() -> None:
    ...

@main.route("/informe_costos/<idComedor>", methods=['GET'])
def informe_costos_comedor(idComedor: int) -> Response:
    ...
