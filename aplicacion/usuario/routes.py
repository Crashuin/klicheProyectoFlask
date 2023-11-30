from flask import redirect, render_template, url_for
from . import usuario
from .forms import UsuarioForm

@usuario.route('/usuario')
def usuarioPage():
    form = UsuarioForm()
    return render_template('usuario.html', form=form)


@usuario.route('/ingresar_usuario', methods=['POST'])
def ingresarUsuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
        return redirect(url_for('usuario.dashboard'))

    return render_template('usuario.html', form=form, mostrar_modal=form.errors)
 