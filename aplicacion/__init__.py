from flask import Flask, render_template
from .config import config



def page_not_found(error):
    return render_template('404.html'), 404

def create_app():
    
    app = Flask(__name__, template_folder='templates')

    app.config.from_object(config['development'])
    
    #Error handlers
    app.register_error_handler(404, page_not_found)

    # Registrar blueprints después de la inicialización de las extensiones
    from .inicio import inicio
    from .auth import auth
    from .categoria import categoria
    from .producto import producto
    from .cliente import cliente
    from .usuario import usuario
    from .venta import venta
    from .dashboard import dashboard

    app.register_blueprint(inicio)
    app.register_blueprint(auth)
    app.register_blueprint(categoria)
    app.register_blueprint(producto)
    app.register_blueprint(cliente)
    app.register_blueprint(usuario)
    app.register_blueprint(venta)
    app.register_blueprint(dashboard)

    return app




