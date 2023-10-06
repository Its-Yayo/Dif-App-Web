#!/usr/bin/python3

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
def login() -> str:
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




