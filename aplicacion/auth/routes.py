from flask import redirect, render_template, url_for, request, flash, current_app


# blueprints
from . import auth

# formulario
from .forms import LoginForm

# modelos
from .models.ModelUser import ModelUser

# entidades
from .models.entities.User import User


@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User('', request.form.get('usuario'), request.form.get('contrasena'), '', '', '', '','')
            print("Usuario formulario:", user)
            loged_user = ModelUser.login(user)
            
            if loged_user != None:
                if loged_user.contrasena:
                    flash('Ingreso exitoso')
                    return redirect(url_for('dashboard.dashboard'))
                else:
                    flash('Contraseña incorrecta')
            else:
                flash('Usuario no encontrado')
                
    return render_template('login.html', form=form)

