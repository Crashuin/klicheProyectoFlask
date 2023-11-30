from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, DataRequired, Email
from wtforms.validators import Length

class ClienteForm(FlaskForm):
    clienteNombre = StringField('Nombre del cliente', validators=[InputRequired(message="Ingrese nombre del cliente")])
    clienteDireccion = StringField('Dirección', validators=[InputRequired(message="Ingrese dirección del cliente")])
    clienteDocumento = StringField('Documento', validators=[InputRequired(message="Ingrese identificación del cliente")])
    clienteEmail = EmailField('Email', validators=[InputRequired(message="Ingrese e-mail del cliente"), Email(message="E-mail no valido")])
    # Otros campos del formulario