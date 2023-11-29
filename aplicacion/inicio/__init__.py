from flask import Blueprint, render_template

inicio = Blueprint('inicio', __name__, template_folder='templates')

from . import routes