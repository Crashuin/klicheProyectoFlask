from flask import redirect, render_template, url_for
from . import auth
from .forms import LoginForm

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

# @auth.route('/login')
# def login():
#     return render_template('login.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
        return redirect(url_for('inicio.dashboard'))

    return render_template('login.html', form=form)
