#!/usr/bin/python3

from typing import Any

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug import Response
import mariadb

main = Blueprint('main', __name__, template_folder='app/templates')


@main.route("/registro_admin", methods=['GET', 'POST'])
def registro_admin() -> Response | Any:
    if request.method == 'POST':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.form['comedor']
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_InsertAdministrador', [id_comedor, request.form['nombre'], request.form['curp'], request.form['username'], request.form['password']])
            conn.commit()

            return redirect(url_for('main.login'))
        except Exception as e:
            flash('Error al registrar', 'error')
            print(e)  # Debug Message
            return render_template("registro.html")

    return render_template("registro.html")

@main.route("/login", methods=['GET', 'POST'])
def login() -> Response | Any:
    if request.method == 'POST':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_LoginAdministrador', (request.form['username'], request.form['password']))
        result = cur.fetchone()

        if result and result[0] == 1:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.tablero'))
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'error')

    return render_template("login.html")


@main.route("/cerrar_sesion", methods=['GET', 'POST'])
def cerrar_sesion() -> Response:
    if request.method == 'POST':
        return redirect(url_for('main.root'))


@main.route("/tablero", methods=['GET'])
def tablero() -> Response:
    return render_template('home.html')


# TODO: Implementation
@main.route("/tablero_afluencia", methods=['POST'])
def tablero_afluencia() -> Response | Any:
    if request.method == 'POST':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.form['comedor']

            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_TableroAfluencia', [id_comedor])
            result = cur.fetchone()

            afluencia_personas = result[0]

            return render_template("tablero.html", afluencia_personas=afluencia_personas)
        except Exception as e:
            flash('Error al obtener la afluencia', 'error')
            print(e)  # Mensaje de depuración
            return render_template("tablero.html")

    return render_template("tablero.html")


@main.route("/tablero/recaudacion/<int:idComedor>", methods=['GET'])
def tablero_recaudacion(idComedor: int):
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroRecaudacion', [idComedor])
        recaudacion = cur.fetchone()

        if recaudacion:
            return render_template('home.html', recaudacion=recaudacion[0])
        else:
            return render_template('home.html', error_message="No se encontraron registros de recaudación para este comedor.")

@main.route("/tablero/afluencia_mes/<int:idComedor>", methods=['GET'])
def tablero_afluencia_mes(idComedor: int):
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroAfluenciaMes', [idComedor])
        afluencia_mes = cur.fetchall()

        if afluencia_mes:
            return render_template('home.html', afluencia_mes=afluencia_mes)
        else:
            return render_template('home.html', error_message="No se encontraron registros de afluencia mensual para este comedor.")

@main.route("/tablero/inscritos/<int:idComedor>", methods=['GET'])
def tablero_inscritos(idComedor: int):
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_TableroInscritos', [idComedor])
        inscritos = cur.fetchall()
        cur.close()

        if inscritos:
            return render_template('home.html', inscritos=inscritos)
        else:
            return render_template('home.html', error_message="No se encontraron empleados registrados para este comedor.")


# TODO: Implementation
@main.route("/recaudaciones", methods=['GET'])
def recaudaciones() -> None:
    return render_template('recaudacion.html')


# TODO: Implementation
@main.route("/recaudaciones/donaciones/<idComedor>", methods=['GET'])
def recaudaciones_donaciones(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesDonaciones', idComedor)
        recaudaciones_donaciones = cur.fetchone()

        return render_template('recaudacion.html', recaudaciones_donaciones=recaudaciones_donaciones)


# TODO: Implementation
@main.route("/recaudaciones/ventas/<idComedor>", methods=['GET'])
def recaudaciones_ventas(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_RecaudacionesVentas', idComedor)
        recaudaciones_ventas = cur.fetchone()

        return render_template('recaudacion.html', recaudaciones_ventas=recaudaciones_ventas)


# TODO: Implementation
@main.route("/personal", methods=['GET'])
def personal() -> None:
    return render_template('personal.html')


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
@main.route("/inventario", methods=['GET'])
def inventario() -> None:
    return render_template('inventario.html')


# TODO: Implementation
@main.route("/inventario/<idComedor>", methods=['GET'])
def inventario_lista(idComedor: int) -> Response | str:
    if request.method == 'GET':
        conn = connection()
        cur = conn.cursor()

        cur.callproc('PROC_InventarioLista', idComedor)
        inventario_lista = cur.fetchone()

        return render_template('inventario.html', inventario_lista=inventario_lista)


# TODO: APIs de la App de Administrador
@main.route("/login_app", methods=['POST'])
def login_app() -> Response | Any:
    data = request.get_json()

    conn = connection()
    cur = conn.cursor()

    cur.callproc('PROC_LoginAdministrador', data['usuario'], data['contraseña'])
    usuario_final = cur.fetchone()

    if usuario_final and usuario_final[0] == 1:
        response = {
            'message': 'Inicio de sesión exitoso',
            'status': 'success'
        }
        return jsonify(response), 201
    else:
        response = {
            'message': 'Credenciales incorrectas. Inténtalo de nuevo.',
            'status': 'error'
        }
        return jsonify(response), 400


@main.route("/registrar_cliente", methods=['POST'])
def registrar_cliente():
    data = request.get_json()

    try:
        if 'curp' in data:
            curp = data['curp']
        else:
            curp = None

        nombre = data['nombre']
        apellido = data['apellido']
        edad = data['edad']
        genero = data['genero']
        circunstancia = data['circunstancia']
        rol = data['rol']

        conn = connection()
        cur = conn.cursor()
        cur.callproc('PROC_AgregarCliente', (nombre, apellido, edad, genero, circunstancia, rol))
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


@main.route("/mostrar_entregas/<idComedor>", methods=['GET'])
def mostrar_entregas(idComedor: int):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.callproc('PROC_MostrarEntregas', idComedor)
        entregas = cur.fetchall()
        conn.close()

        response = {
            'message': 'Entregas mostradas exitosamente',
            'status': 'success',
            'entregas': entregas
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'message': 'Error al mostrar entregas',
            'status': 'error',
            'error': str(e)
        }
        return jsonify(response), 500


@main.route("/mostrar_donativos/<idComedor>", methods=['GET'])
def mostrar_donativos(idComedor: int):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.callproc('PROC_MostrarDonativos', idComedor)
        donativos = cur.fetchall()
        conn.close()

        response = {
            'message': 'Donativos mostrados exitosamente',
            'status': 'success',
            'donativos': donativos
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'message': 'Error al mostrar donativos',
            'status': 'error',
            'error': str(e)
        }
        return jsonify(response), 500



# --------------------------------------------

@main.route("/")
def root() -> str:
    return render_template("login.html")
