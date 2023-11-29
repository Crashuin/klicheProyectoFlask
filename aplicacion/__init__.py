from flask import Flask
from .auth import auth
from .categoria import categoria
from .producto import producto
from .cliente import cliente
from .usuario import usuario
from .venta import venta
from .inicio import inicio

app = Flask(__name__)
app.config.from_pyfile('config/configuracion.cfg')

app.register_blueprint(auth)
app.register_blueprint(categoria)
app.register_blueprint(producto)
app.register_blueprint(cliente)
app.register_blueprint(usuario)
app.register_blueprint(venta)
app.register_blueprint(inicio)


