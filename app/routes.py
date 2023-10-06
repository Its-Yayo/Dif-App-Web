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

@main.route("/login")
def login() -> str:
    ...

@main.route("/error")
def error() -> str:
    ...


