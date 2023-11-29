from flask import render_template
from . import categoria

@categoria.route('/categoria')
def categoriaPage():
    return render_template('categoria.html')


    