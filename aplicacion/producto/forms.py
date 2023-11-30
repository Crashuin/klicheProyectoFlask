from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired

class ProductoForm(FlaskForm):
    opciones_categoria = [('seleccione', 'Seleccione categoría'), ('categoria1', 'Categoría 1'), ('categoria2', 'Categoría 2')]
    productoCategoria = SelectField('Categoría del producto', choices=opciones_categoria, validators=[InputRequired(message="Ingrese una categoría")])

    productoNombre = StringField('Nombre del producto', validators=[InputRequired(message="Ingrese nombre del producto")])
    productoDescripcion = TextAreaField('Descripción del producto', validators=[InputRequired(message="Ingrese una descripción")])
    productoImagen = FileField('Imagen del producto', validators=[InputRequired(message="El producto necesita una imagen")])
    productoPrecio = StringField('Precio de venta', validators=[InputRequired(message="El precio no debe ir vacio")])
    # Otros campos del formulario