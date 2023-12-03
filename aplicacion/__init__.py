from flask import Flask, render_template, redirect, url_for
from .config import config

#formulario
from flask_wtf.csrf import CSRFProtect

# Registrar blueprints 
from .inicio import inicio
from .auth import auth
from .categoria import categoria
from .producto import producto
from .cliente import cliente
from .usuario import usuario
from .venta import venta
from .dashboard import dashboard

# Models:
from .auth.models.ModelUser import ModelUser

#flask-login
from flask_login import LoginManager, login_user, logout_user, login_required

def page_not_found(error):
    return render_template('404.html'), 404

def status_401(error):
    return redirect(url_for('auth.login'))

def create_app():

    app = Flask(__name__, template_folder='templates')

    #csrf
    csrf = CSRFProtect()
    csrf.init_app(app)

    #Cargar usuario y sesión
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(id):
        return ModelUser.get_by_id(id)
    
    #registrar blueprints
    app.register_blueprint(inicio)
    app.register_blueprint(auth)
    app.register_blueprint(categoria)
    app.register_blueprint(producto)
    app.register_blueprint(cliente)
    app.register_blueprint(usuario)
    app.register_blueprint(venta)
    app.register_blueprint(dashboard)

    #configuracion
    app.config.from_object(config['development'])
    
    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, status_401)

    return app




