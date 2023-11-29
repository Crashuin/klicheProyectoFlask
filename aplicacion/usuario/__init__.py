from flask import Blueprint, render_template

usuario = Blueprint('usuario', __name__, template_folder='templates', static_folder='static/css')

from . import routes