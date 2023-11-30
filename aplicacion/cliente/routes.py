from flask import redirect, render_template, url_for
from . import cliente
from .forms import ClienteForm
from flask import url_for


@cliente.route('/cliente', methods=['GET'])
def clientePage():
    form = ClienteForm()
    return render_template('cliente.html', form=form)   

@cliente.route('/ingresar_cliente', methods=['POST'])
def ingresarCliente():
    form = ClienteForm()
    if form.validate_on_submit():
        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
        return redirect(url_for('cliente.dashboard'))

    return render_template('cliente.html', form=form, mostrar_modal=form.errors)