#!/usr/bin/python3

from typing import Any

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug import Response
import mariadb

main = Blueprint('main', __name__, template_folder='app/templates')


@main.route("/login", methods=['GET', 'POST'])
def login() -> Response | Any:
    if request.method == 'POST':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_Login', request.form['usuario'], request.form['contraseña'])
        usuario_final = cur.fetchone()

        if usuario_final and usuario_final[0] == 1:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('tablero'))
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'error')

    return render_template("login.html")


@main.route("/cerrar_sesion", methods=['GET', 'POST'])
def cerrar_sesion() -> Response:
    if request.method == 'POST':
        return redirect(url_for('main.root'))


@main.route("/tablero", methods=['GET'])
def tablero() -> None:
    render_template('tablero.html')


# TODO: Implementation
@main.route("/tablero/afluencia/<string:idComedor>", methods=['GET'])
def tablero_afluencia(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluencia', idComedor)
        afluencia = cur.fetchone()

        return render_template('tablero.html', afluencia=afluencia)


# TODO: Implementation
@main.route("/tablero/recaudacion", methods=['GET'])
def tablero_recaudacion() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroRecaudacion')
        recaudacion = cur.fetchone()

        return render_template('tablero.html', recaudacion=recaudacion)


# TODO: Implementation
@main.route("/tablero/afluencia_año", methods=['GET'])
def tablero_afluencia_year() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluenciaAño')
        afluencia_year = cur.fetchone()

        return render_template('tablero.html', afluencia_year=afluencia_year)


# TODO: Implementation
@main.route("/tablero/afluencia_comedores", methods=['GET'])
def tablero_comedores() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluenciaComedores')
        afluencia_comedores = cur.fetchone()

        return render_template('tablero.html', afluencia_comedores=afluencia_comedores)


# TODO: Implementation
@main.route("/afluencia", methods=['GET'])
def afluencia() -> None:
    render_template('afluencia.html')


# TODO: Implementation
@main.route("/afluencia/<idComedor>/<tiempo>", methods=['GET'])
def afluencia_registros(idComedor: int, tiempo: str) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaRegistros', idComedor, tiempo)
        afluencia = cur.fetchone()

        return render_template('afluencia.html', afluencia=afluencia)


# TODO: Implementation
@main.route("/afluencia/inscritos/<idComedor>", methods=['GET'])
def afluencia_inscritos(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaInscritos', idComedor)
        afluencia_inscritos = cur.fetchone()

        return render_template('afluencia.html', afluencia_inscritos=afluencia_inscritos)


# TODO: Implementation
@main.route("/afluencia/predicciones/idComedor>", methods=['GET'])
def afluencia_predicciones(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AfluenciaPredicciones', idComedor)
        afluencia_predicciones = cur.fetchone()

        return render_template('afluencia.html', afluencia_predicciones=afluencia_predicciones)


# TODO: Implementation
@main.route("/recaudaciones", methods=['GET'])
def recaudaciones() -> None:
    render_template('recaudaciones.html')


# TODO: Implementation
@main.route("/recaudaciones/<idComedor>/<tiempo>", methods=['GET'])
def recaudaciones_registros(idComedor: int, tiempo: str) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesRegistros', idComedor, tiempo)
        recaudaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones=recaudaciones)


# TODO: Implementation
@main.route("/recaudaciones/donaciones/<idComedor>", methods=['GET'])
def recaudaciones_donaciones(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesDonaciones', idComedor)
        recaudaciones_donaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_donaciones=recaudaciones_donaciones)


# TODO: Implementation
@main.route("/recaudaciones/ventas/<idComedor>", methods=['GET'])
def recaudaciones_ventas(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesVentas', idComedor)
        recaudaciones_ventas = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_ventas=recaudaciones_ventas)


# TODO: Implementation
@main.route("/recaudaciones/lista_donaciones/", methods=['GET'])
def recaudaciones_lista_donaciones() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesListaDonaciones')
        recaudaciones_lista_donaciones = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_lista_donaciones=recaudaciones_lista_donaciones)


# TODO: Implementation
@main.route("/recaudaciones/lista_ventas/", methods=['GET'])
def recaudaciones_lista_ventas() -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesListaVentas')
        recaudaciones_lista_ventas = cur.fetchone()

        return render_template('recaudaciones.html', recaudaciones_lista_ventas=recaudaciones_lista_ventas)


# TODO: Implementation
@main.route("/personal", methods=['GET'])
def personal() -> None:
    render_template('personal.html')


# TODO: Implementation
@main.route("/personal/lista_personal/<idComedor>", methods=['GET'])
def personal_lista(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_PersonalLista', idComedor)
        personal_lista = cur.fetchone()

        return render_template('personal.html', personal_lista=personal_lista)


# TODO: Implementation
@main.route("/invetario", methods=['GET'])
def inventario() -> None:
    render_template('inventario.html')


# TODO: Implementation
@main.route("/inventario/lista_inventario/<idComedor>", methods=['GET'])
def inventario_lista(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_InventarioLista', idComedor)
        inventario_lista = cur.fetchone()

        return render_template('inventario.html', inventario_lista=inventario_lista)


# TODO: APIs de las Apps móviles
@main.route("/login_app", methods=['POST'])
def login_app() -> Response | Any:
    data = request.get_json()

    conn = connection()
    cur = conn.cursor()

    cur.callproc('PROC_Login', data['usuario'], data['contraseña'])
    usuario_final = cur.fetchone()

    if usuario_final and usuario_final[0] == 1:
        response = {
            'message': 'Inicio de sesión exitoso',
            'status': 'success'
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Credenciales incorrectas. Inténtalo de nuevo.',
            'status': 'error'
        }
        return jsonify(response), 401


@main.route("/registrar_cliente", methods=['POST'])
def registrar_cliente():
    try:
        if 'curp' in request.form:
            curp = request.form['curp']
        else:
            curp = None

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        genero = request.form['genero']
        circunstancia = request.form['circunstancia']
        rol = request.form['rol']

        conn = connection()
        cur = conn.cursor()
        cur.callproc('PROC_AgregarUsuario', (nombre, apellido, edad, genero, circunstancia, rol))
        conn.commit()
        conn.close()

        response = {
            'message': 'Usuario agregado exitosamente',
            'status': 'success'
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'message': 'Error al agregar usuario',
            'status': 'error',
            'error': str(e)
        }
        return jsonify(response), 500

@main.route("/registrar_empleado", methods=['POST'])
def registrar_empleado():
    try:
        if 'curp' in request.form:
            curp = request.form['curp']
        else:
            curp = None

        comedor = request.form['comedor']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        genero = request.form['genero']
        circunstancia = request.form['circunstancia']

        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_AgregarEmpleado', (curp, comedor, nombre, apellido, edad, genero, circunstancia))
        conn.commit()

        response = {
            'message': 'Empleado agregado exitosamente',
            'status': 'success'
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'message': 'Error al agregar empleado',
            'status': 'error',
            'error': str(e)
        }
        return jsonify(response), 500


# --------------------------------------------

@main.route("/")
def root() -> str:
    return render_template("login.html")
