from flask import redirect, render_template, url_for
from . import producto
from .forms import ProductoForm

from flask_login import login_user, login_manager, logout_user, login_required

@producto.route('/producto', methods=['GET'])
@login_required
def productoPage():
    form = ProductoForm()
    return render_template('producto.html', form=form)

@producto.route('/ingresar_producto', methods=['POST'])
@login_required
def ingresarProducto():
    form = ProductoForm()
    if form.validate_on_submit():
        return redirect(url_for('producto.productoPage'))
    return render_template('producto.html', form=form, mostrar_modal=form.errors)