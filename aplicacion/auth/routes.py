from flask import redirect, render_template, url_for, request, flash, current_app


# blueprints
from . import auth

# formulario
from .forms import LoginForm

# modelos
from .models.ModelUser import ModelUser

# entidades
from .models.entities.User import User
from flask_login import current_user, login_user, login_manager, logout_user, login_required

#logs
import logging

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User('', request.form.get('usuario'), request.form.get('contrasena'), '', '', '', '','')
            loged_user = ModelUser.login(user)
            
            if loged_user != None:
                if loged_user.contrasena:
                    login_user(loged_user)
                    logging.info(f"Usuario {current_user.usuario} ha iniciado sesión")
                    return redirect(url_for('dashboard.dashboard'))
                else:
                    flash('Contraseña incorrecta')
            else:
                flash('Usuario no encontrado')
                
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logging.info(f"Usuario {current_user.usuario} ha cerrado sesión")
    logout_user()
    return redirect(url_for('auth.login'))

