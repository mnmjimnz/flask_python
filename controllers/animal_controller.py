from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.animal_model import AnimalModel

animal_bp = Blueprint('animals', __name__)

@animal_bp.route('/')
def home():
    """Redirecciona a la vista principal del listado."""
    return redirect(url_for('animals.index'))

@animal_bp.route('/animales')
def index():
    """Controlador: Muestra la lista de todos los animales registrados para citas."""
    try:
        animales = AnimalModel.get_all()
        return render_template('animals/index.html', animales=animales)
    except Exception as e:
        flash(f"Error al conectar con la base de datos MySQL: {str(e)}", "danger")
        return render_template('animals/index.html', animales=[], db_error=True)

@animal_bp.route('/animales/nuevo', methods=['GET', 'POST'])
def create():
    """Controlador: Formulario y lógica para registrar un animal para su cita."""
    if request.method == 'POST':
        # Extracción y limpieza de datos
        nombre_mascota = request.form.get('nombre_mascota', '').strip()
        especie = request.form.get('especie', '').strip()
        raza = request.form.get('raza', '').strip()
        edad = request.form.get('edad', '').strip()
        sexo = request.form.get('sexo', '').strip()
        nombre_propietario = request.form.get('nombre_propietario', '').strip()
        telefono_propietario = request.form.get('telefono_propietario', '').strip()
        fecha_cita = request.form.get('fecha_cita', '').strip()
        hora_cita = request.form.get('hora_cita', '').strip()
        motivo_cita = request.form.get('motivo_cita', '').strip()

        # Validación básica en backend
        campos_obligatorios = [
            ('Nombre de la mascota', nombre_mascota),
            ('Especie', especie),
            ('Raza', raza),
            ('Edad', edad),
            ('Sexo', sexo),
            ('Propietario', nombre_propietario),
            ('Teléfono', telefono_propietario),
            ('Fecha de cita', fecha_cita),
            ('Hora de cita', hora_cita),
            ('Motivo de cita', motivo_cita)
        ]

        faltantes = [campo for campo, valor in campos_obligatorios if not valor]
        if faltantes:
            flash(f"Por favor completa los siguientes campos: {', '.join(faltantes)}.", "warning")
            return render_template('animals/create.html', form_data=request.form)

        datos = {
            'nombre_mascota': nombre_mascota,
            'especie': especie,
            'raza': raza,
            'edad': edad,
            'sexo': sexo,
            'nombre_propietario': nombre_propietario,
            'telefono_propietario': telefono_propietario,
            'fecha_cita': fecha_cita,
            'hora_cita': hora_cita,
            'motivo_cita': motivo_cita
        }

        try:
            AnimalModel.create(datos)
            flash("¡Animal registrado exitosamente para su cita médica!", "success")
            return redirect(url_for('animals.index'))
        except Exception as e:
            flash(f"Error al guardar el registro en MySQL: {str(e)}", "danger")
            return render_template('animals/create.html', form_data=request.form)

    # Petición GET: muestra formulario vacío
    return render_template('animals/create.html', form_data={})

@animal_bp.route('/animales/editar/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Controlador: Edición de un registro existente de animal y cita."""
    animal = AnimalModel.get_by_id(id)
    if not animal:
        flash("El registro solicitado no existe o fue eliminado.", "warning")
        return redirect(url_for('animals.index'))

    if request.method == 'POST':
        nombre_mascota = request.form.get('nombre_mascota', '').strip()
        especie = request.form.get('especie', '').strip()
        raza = request.form.get('raza', '').strip()
        edad = request.form.get('edad', '').strip()
        sexo = request.form.get('sexo', '').strip()
        nombre_propietario = request.form.get('nombre_propietario', '').strip()
        telefono_propietario = request.form.get('telefono_propietario', '').strip()
        fecha_cita = request.form.get('fecha_cita', '').strip()
        hora_cita = request.form.get('hora_cita', '').strip()
        motivo_cita = request.form.get('motivo_cita', '').strip()

        campos_obligatorios = [
            ('Nombre de la mascota', nombre_mascota),
            ('Especie', especie),
            ('Raza', raza),
            ('Edad', edad),
            ('Sexo', sexo),
            ('Propietario', nombre_propietario),
            ('Teléfono', telefono_propietario),
            ('Fecha de cita', fecha_cita),
            ('Hora de cita', hora_cita),
            ('Motivo de cita', motivo_cita)
        ]

        faltantes = [campo for campo, valor in campos_obligatorios if not valor]
        if faltantes:
            flash(f"Por favor completa los siguientes campos: {', '.join(faltantes)}.", "warning")
            return render_template('animals/edit.html', animal=request.form, animal_id=id)

        datos = {
            'nombre_mascota': nombre_mascota,
            'especie': especie,
            'raza': raza,
            'edad': edad,
            'sexo': sexo,
            'nombre_propietario': nombre_propietario,
            'telefono_propietario': telefono_propietario,
            'fecha_cita': fecha_cita,
            'hora_cita': hora_cita,
            'motivo_cita': motivo_cita
        }

        try:
            AnimalModel.update(id, datos)
            flash("¡Registro del animal y cita actualizado correctamente!", "success")
            return redirect(url_for('animals.index'))
        except Exception as e:
            flash(f"Error al actualizar en la base de datos: {str(e)}", "danger")
            return render_template('animals/edit.html', animal=request.form, animal_id=id)

    # Petición GET: muestra formulario con datos precargados
    return render_template('animals/edit.html', animal=animal, animal_id=id)

@animal_bp.route('/animales/eliminar/<int:id>', methods=['POST'])
def delete(id):
    """Controlador: Elimina un registro de animal y cita."""
    try:
        eliminado = AnimalModel.delete(id)
        if eliminado:
            flash("¡Registro eliminado correctamente!", "success")
        else:
            flash("No se encontró el registro para eliminar.", "warning")
    except Exception as e:
        flash(f"Error al eliminar de la base de datos: {str(e)}", "danger")

    return redirect(url_for('animals.index'))
