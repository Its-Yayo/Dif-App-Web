#!/usr/bin/env python3

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
@main.route("/tablero_afluencia", methods=['GET'])
def tablero_afluencia() -> Response | Any:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_TableroAfluencia', [id_comedor])
            result = cur.fetchone()

            afluencia_personas = result[0]

            return jsonify({'afluencia_dia': afluencia_personas})
        except Exception as e:
            flash('Error al obtener la afluencia', 'error')
            print(e)  # Mensaje de depuración
            return jsonify({'error': 'Error al obtener la afluencia'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})


@main.route("/tablero_recaudacion", methods=['GET'])
def tablero_recaudacion():
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_TableroRecaudacion', [id_comedor])
            recaudacion = cur.fetchone()
            recaudaciones = recaudacion[0]

            return jsonify({'recaudacion_dia': recaudaciones})
        except Exception as e:
            flash('Error al obtener la recaudación', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener la recaudación'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})


@main.route("/tablero_inscritos", methods=['GET'])
def tablero_inscritos() -> Response | str:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_TableroInscritos', [id_comedor])
            inscritos = cur.fetchall()

            return render_template('home.html', empleados=inscritos)
        except Exception as e:
            flash('Error al obtener los inscritos', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener los inscritos'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})




# TODO: Implementation
@main.route("/recaudaciones", methods=['GET'])
def recaudaciones() -> None:
    return render_template('recaudacion.html')


# TODO: Implementation
@main.route("/recaudaciones_donaciones", methods=['GET'])
def recaudaciones_donaciones() -> Response | str:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_RecaudacionesDonaciones', [id_comedor])
            result = cur.fetchone()

            return jsonify({'recaudaciones_donaciones': result[0]})
        except Exception as e:
            flash('Error al obtener las recaudaciones', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener las recaudaciones'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})


# TODO: Implementation
@main.route("/recaudaciones_ventas", methods=['GET'])
def recaudaciones_ventas() -> Response | str:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_RecaudacionesVentas', [id_comedor])
            result = cur.fetchone()

            return jsonify({'recaudaciones_ventas': result[0]})
        except Exception as e:
            flash('Error al obtener las recaudaciones', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener las recaudaciones'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})

# TODO: Implementation
@main.route("/personal", methods=['GET'])
def personal() -> None:
    return render_template('personal.html')


# TODO: Implementation
@main.route("/personal_lista", methods=['GET'])
def personal_lista() -> Response | str:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')
            cur.callproc('PROC_PersonalLista', [comedor_seleccionado])
            admin = cur.fetchall()

            if admin:
                personal_lista = {'nombre': admin[0][0], 'curp': admin[0][1]}
                return jsonify(personal_lista)
            else:
                return jsonify({'error': 'No se encontró administrador para el comedor seleccionado'})
        except Exception as e:
            flash('Error al obtener el administrador', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener el administrador'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})


# TODO: Implementation
@main.route("/inventario", methods=['GET'])
def inventario() -> None:
    return render_template('inventario.html')


@main.route("/inventario_lista", methods=['GET'])
def inventario_lista() -> Response | str:
    if request.method == 'GET':
        try:
            conn = connection()
            cur = conn.cursor()

            comedor_seleccionado = request.args.get('comedor')

            print(f"Comedor seleccionado: {comedor_seleccionado}")

            cur.execute("SELECT idComedor FROM Comedor WHERE nombre = %s", (comedor_seleccionado,))
            id_comedor = cur.fetchone()[0]

            cur.callproc('PROC_InventarioLista', [comedor_seleccionado])
            productos = cur.fetchall()

            if productos:
                lista_productos = [{'cantidad': producto[0], 'descripcion': producto[1], 'presentacion': producto[2],
                                    'unidadMedida': producto[3]} for producto in productos]
                return jsonify({'productos': lista_productos})
            else:
                return jsonify({'error': 'No se encontraron productos para el comedor seleccionado'})
        except Exception as e:
            flash('Error al obtener la lista de productos', 'error')
            print(e)
            return jsonify({'error': 'Error al obtener la lista de productos'})

    return jsonify({'error': 'Método GET no permitido en esta ruta'})


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

'''
@main.route("/inventario_app", methods=['GET'])
def inventario_app() -> Any | Response:
    if request.method == 'GET':
        try:
            ...
        except exception as e:
            ...
        
'''



'''
@main.route("/pruebas", methods=['GET'])
def pruebas() -> Response | str:
    return render_template('pruebas.html')


@main.route("/img_cerrar_sesion", methods=['GET'])
def img_cerrar_sesion() -> Response | str:
    return render_template('../images/cerrar-sesion.png')

@main.route("/img_logo_atzp", methods=['GET'])
def img_logo_atzp() -> str:
    return render_template('../images/logo_atzp.png')

@main.route("/img_multitud", methods=['GET'])
def img_multitud() -> str:
    return render_template('../images/multitud.png')


@main.route("/img_personal", methods=['GET'])
def img_personal() -> str:
    return render_template('../images/personal.png')


@main.route("/img_rentable", methods=['GET'])
def img_rentable() -> Response | str:
    return render_template('../images/rentable.png')


@main.route("/img_comedor", methods=['GET'])
def img_comedor() -> Response | str:
    return render_template('../images/comedor.png')


@main.route("/img_tablero", methods=['GET'])
def img_tablero() -> str:
    return render_template('../images/tablero.png')


@main.route("/img_inventario", methods=['GET'])
def img_inventario() -> str:
    return render_template('../images/inventario.png')


@main.route("/img_estadisticas", methods=['GET'])
def img_cerrar_sesion() -> Response | str:
    return render_template('../images/estadisticas.png')'''





# --------------------------------------------

@main.route("/")
def root() -> str:
    return render_template("login.html")
