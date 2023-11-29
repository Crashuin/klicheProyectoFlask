from flask import render_template
from . import producto

@producto.route('/producto')
def productoPage():
    return render_template('producto.html')