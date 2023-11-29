from flask import render_template
from . import usuario

@usuario.route('/usuario')
def usuarioPage():
    return render_template('usuario.html')