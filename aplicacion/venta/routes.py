from flask import render_template
from . import venta

@venta.route('/venta')
def ventaPage():
    return render_template('venta.html')