from flask import redirect, render_template, url_for
from . import categoria
from .forms import CategoriaForm

@categoria.route('/categoria', methods=['GET'])
def categoriaPage():
    form = CategoriaForm()
    return render_template('categoria.html', form=form)

@categoria.route('/ingresar_categoria', methods=['POST'])
def ingresarCategoria():
    form = CategoriaForm()
    if form.validate_on_submit():
        # Aquí puedes manejar la lógica de inicio de sesión con los datos del formulario
        # Por ejemplo, podrías verificar las credenciales y redirigir al usuario
        return redirect(url_for('categoria.dashboard'))

    return render_template('categoria.html', form=form, mostrar_modal=form.errors)
 