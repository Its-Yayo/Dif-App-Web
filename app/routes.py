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

# --------------------------------------------------------------------

# Routes coming ahead

@main.route("/login", methods=['GET', 'POST'])
def login() -> Response | Any:
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
