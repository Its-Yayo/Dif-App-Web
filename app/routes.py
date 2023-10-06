#!/usr/bin/python3

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug import Response
import mariadb

main = Blueprint('main', __name__, template_folder='app/templates')


