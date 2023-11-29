from flask import render_template
from . import cliente


@cliente.route('/cliente')
def clientePage():
    return render_template('cliente.html')