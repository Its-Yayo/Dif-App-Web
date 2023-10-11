#!/usr/bin/python3

from typing import Any

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug import Response
import mariadb

main = Blueprint('main', __name__, template_folder='app/templates')


@main.route("/")
def main() -> str:
    return render_template("login.html")


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

    return render_template("login.html")


@main.route("/cerrar_sesion", methods=['GET', 'POST'])
def cerrar_sesion() -> Response:
    if request.method == 'POST':
        return redirect(url_for('main'))


@main.route("/tablero", methods=['GET'])
def tablero() -> None:
    render_template('tablero.html')


@main.route("/tablero/afluencia/<string:idComedor>", methods=['GET'])
def tablero_afluencia(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluencia', idComedor)
        afluencia = cur.fetchone()

        return render_template('tablero.html', afluencia=afluencia)


@main.route("/tablero/recaudacion", methods=['GET'])
def tablero_recaudacion() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroRecaudacion')
        recaudacion = cur.fetchone()

        return render_template('tablero.html', recaudacion=recaudacion)


@main.route("/tablero/afluencia_año", methods=['GET'])
def tablero_afluencia_year() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluenciaAño')
        afluencia_year = cur.fetchone()

        return render_template('tablero.html', afluencia_year=afluencia_year)


@main.route("/tablero/afluencia_comedores", methods=['GET'])
def tablero_comedores() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluenciaComedores')
        afluencia_comedores = cur.fetchone()

        return render_template('tablero.html', afluencia_comedores=afluencia_comedores)


@main.route("/afluencia", methods=['GET'])
def afluencia() -> None:
    render_template('afluencia.html')


@main.route("/afluencia/<idComedor>/<tiempo>", methods=['GET'])
def afluencia_registros(idComedor: int, tiempo: str) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaRegistros', idComedor, tiempo)
        afluencia = cur.fetchone()

        return render_template('afluencia.html', afluencia=afluencia)


@main.route("/afluencia/inscritos/<idComedor>", methods=['GET'])
def afluencia_inscritos(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaInscritos', idComedor)
        afluencia_inscritos = cur.fetchone()

        return render_template('afluencia.html', afluencia_inscritos=afluencia_inscritos)


@main.route("/afluencia/predicciones/idComedor>", methods=['GET'])
def afluencia_predicciones(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaPredicciones', idComedor)
        afluencia_predicciones = cur.fetchone()

        return render_template('afluencia.html', afluencia_predicciones=afluencia_predicciones)


@main.route("/recaudaciones", methods=['GET'])
def recaudaciones() -> None:
    render_template('recaudaciones.html')


@main.route("/recaudaciones/<idComedor>/<tiempo>", methods=['GET'])
def recaudaciones_registros(idComedor: int, tiempo: str) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesRegistros', idComedor, tiempo)
        recaudaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones=recaudaciones)


@main.route("/recaudaciones/donaciones/<idComedor>", methods=['GET'])
def recaudaciones_donaciones(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesDonaciones', idComedor)
        recaudaciones_donaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_donaciones=recaudaciones_donaciones)


@main.route("/recaudaciones/ventas/<idComedor>", methods=['GET'])
def recaudaciones_ventas(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesVentas', idComedor)
        recaudaciones_ventas = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_ventas=recaudaciones_ventas)


@main.route("/recaudaciones/lista_donaciones/", methods=['GET'])
def recaudaciones_lista_donaciones() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesListaDonaciones')
        recaudaciones_lista_donaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_lista_donaciones=recaudaciones_lista_donaciones)


@main.route("/recaudaciones/lista_ventas/", methods=['GET'])
def recaudaciones_lista_ventas() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesListaVentas')
        recaudaciones_lista_ventas = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_lista_ventas=recaudaciones_lista_ventas)


@main.route("/personal", methods=['GET'])
def personal() -> None:
    render_template('personal.html')


@main.route("/personal/lista_personal/<idComedor>", methods=['GET'])
def personal_lista(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_PersonalLista', idComedor)
        personal_lista = cur.fetchone()

        return render_template('personal.html', personal_lista=personal_lista)



@main.route("/invetario", methods=['GET'])
def inventario() -> None:
    render_template('inventario.html')


@main.route("/inventario/lista_inventario/<idComedor>", methods=['GET'])
def inventario_lista(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_InventarioLista', idComedor)
        inventario_lista = cur.fetchone()

        return render_template('inventario.html', inventario_lista=inventario_lista)


# TODO: APIs de las Apps móviles
@main.route("/agregar_asuario/<idComedor", methods=['GET', 'POST'])
def agregar_usuario() -> None:



@main.route("/personal/agregar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_agregar(idComedor: int) -> Response:
    ...


@main.route("/personal/eliminar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_eliminar(idComedor: int) -> Response:
    ...


@main.route("/personal/modificar_personal/<idComedor>", methods=['POST', 'GET'])
def personal_modificar(idComedor: int) -> Response:
    ...

