from flask import redirect, render_template, url_for
from . import venta
from .forms import VentaForm

@venta.route('/venta')
def ventaPage():
    form = VentaForm()
    return render_template('venta.html', form=form)

@venta.route('/venta', methods=['POST'])
def ingresarVenta():
    form = VentaForm()
    if form.validate_on_submit():
        return redirect(url_for('venta.ventaPage'))
    return render_template('venta.html', form=form, mostrar_modal=form.errors)