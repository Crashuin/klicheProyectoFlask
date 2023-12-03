from flask import redirect, render_template, url_for, request, current_app, flash
from .forms import UsuarioForm
from datetime import datetime

from . import usuario




@usuario.route('/usuario')
def usuarioPage():
    form = UsuarioForm()
    return render_template('usuario.html', form=form)

@usuario.route('/ingresar_usuario', methods=['POST'])
def ingresarUsuario():
    form = UsuarioForm()
    if form.validate_on_submit():
      
        flash('Usuario creado exitosamente', 'success')
        return redirect(url_for('usuario.dashboard'))

    return render_template('usuario.html', form=form, mostrar_modal=form.errors)

