from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

class UsuarioForm(FlaskForm):
    usuarioNombre = StringField('Nombre del usuario', validators=[InputRequired(message="Ingrese nombre del usuario")])
    usuario = StringField('Nombre de usuario', validators=[InputRequired(message="Ingrese apodo del usuario")])

    opciones_perfil = [('','Seleccione una opción'),('administrador', 'Administrador')]
    usuarioPerfil = SelectField('Perfil del usuario', choices=opciones_perfil, validators=[InputRequired(message="Seleccione un perfil del usuario")])


    opciones_estado = [('','Seleccione una opción'),('activo', 'Activo'), ('inactivo', 'Inactivo')]
    usuarioEstado = SelectField('Estado del usuario', choices=opciones_estado, validators=[InputRequired(message="Seleccione un estado del usuario")])

    # usuarioEstado = StringField('Estado', validators=[InputRequired(message="El usuario debe tener un estado")])
"""     usuarioUltimoLogin = StringField('Último login', validators=[InputRequired()]) """

