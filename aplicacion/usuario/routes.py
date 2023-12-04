from flask import redirect, render_template, url_for, request, current_app, flash
from .forms import UsuarioForm
from datetime import datetime

# blueprints
from . import usuario

# modelos
from .models.UserModel import UserModel

#entidades
from .models.entities.UserEntity import User

from flask_login import login_user, login_manager, logout_user, login_required

@usuario.route('/usuario')
@login_required
def usuarioPage():
    form = UsuarioForm()
    usuarios = UserModel.listar_usuarios()
    return render_template('usuario.html', form=form, usuarios=usuarios)

@usuario.route('/ingresar_usuario', methods=['POST'])
@login_required
def ingresarUsuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        user = User('', request.form.get('usuarioNombre'), request.form.get('usuario'), request.form.get('contrasena'), request.form.get('usuarioPerfil'), request.form.get('usuarioEstado'),'','')
        usuario_registrado = UserModel.register(user)

        if usuario_registrado:
            flash('Usuario registrado correctamente')
            print(usuario_registrado)
        else:
            print("Usuario no registrado")

        return redirect(url_for('usuario.usuarioPage'))

    return render_template('usuario.html', form=form, mostrar_modal=form.errors)

