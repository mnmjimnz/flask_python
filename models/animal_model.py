from database import get_db_connection
import pymysql

class AnimalModel:
    """
    Modelo MVC para la entidad de registro de animales para citas.
    Maneja todas las operaciones SQL sobre la tabla registro_citas_animales.
    """

    @staticmethod
    def get_all():
        """Obtiene todos los registros de animales y sus citas ordenados cronológicamente."""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT id, nombre_mascota, especie, raza, edad, sexo, 
                           nombre_propietario, telefono_propietario, 
                           fecha_cita, hora_cita, motivo_cita, creado_en
                    FROM registro_citas_animales
                    ORDER BY fecha_cita ASC, hora_cita ASC
                """
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            connection.close()

    @staticmethod
    def get_by_id(animal_id):
        """Busca y retorna un registro específico por su ID."""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    SELECT id, nombre_mascota, especie, raza, edad, sexo, 
                           nombre_propietario, telefono_propietario, 
                           fecha_cita, hora_cita, motivo_cita, creado_en
                    FROM registro_citas_animales
                    WHERE id = %s
                """
                cursor.execute(sql, (animal_id,))
                return cursor.fetchone()
        finally:
            connection.close()

    @staticmethod
    def create(data):
        """
        Inserta un nuevo registro de animal para cita médica.
        Retorna el ID del registro insertado.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO registro_citas_animales 
                    (nombre_mascota, especie, raza, edad, sexo, 
                     nombre_propietario, telefono_propietario, 
                     fecha_cita, hora_cita, motivo_cita)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    data['nombre_mascota'].strip(),
                    data['especie'].strip(),
                    data['raza'].strip(),
                    data['edad'].strip(),
                    data['sexo'].strip(),
                    data['nombre_propietario'].strip(),
                    data['telefono_propietario'].strip(),
                    data['fecha_cita'],
                    data['hora_cita'],
                    data['motivo_cita'].strip()
                )
                cursor.execute(sql, values)
                connection.commit()
                return cursor.lastrowid
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @staticmethod
    def update(animal_id, data):
        """Actualiza los datos de un registro de animal y su cita."""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE registro_citas_animales
                    SET nombre_mascota = %s,
                        especie = %s,
                        raza = %s,
                        edad = %s,
                        sexo = %s,
                        nombre_propietario = %s,
                        telefono_propietario = %s,
                        fecha_cita = %s,
                        hora_cita = %s,
                        motivo_cita = %s
                    WHERE id = %s
                """
                values = (
                    data['nombre_mascota'].strip(),
                    data['especie'].strip(),
                    data['raza'].strip(),
                    data['edad'].strip(),
                    data['sexo'].strip(),
                    data['nombre_propietario'].strip(),
                    data['telefono_propietario'].strip(),
                    data['fecha_cita'],
                    data['hora_cita'],
                    data['motivo_cita'].strip(),
                    animal_id
                )
                cursor.execute(sql, values)
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @staticmethod
    def delete(animal_id):
        """Elimina un registro de animal y cita por su ID."""
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM registro_citas_animales WHERE id = %s"
                cursor.execute(sql, (animal_id,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
