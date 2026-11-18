import pymysql
import pymysql.cursors
from config import Config

def get_db_connection():
    """
    Establece y retorna una conexión a la base de datos MySQL 8.4.11.
    Soporta conexiones locales y remotas con SSL para despliegues en producción (Render).
    """
    try:
        connect_kwargs = {
            'host': Config.DB_HOST,
            'port': Config.DB_PORT,
            'user': Config.DB_USER,
            'password': Config.DB_PASSWORD,
            'database': Config.DB_NAME,
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
            'autocommit': False,
            'connect_timeout': 10
        }

        # Si se requiere SSL para bases de datos remotas en la nube (ej. TiDB, Aiven, Railway)
        if Config.DB_SSL:
            connect_kwargs['ssl'] = {'ssl_mode': 'PREFERRED'}

        connection = pymysql.connect(**connect_kwargs)
        return connection
    except pymysql.MySQLError as err:
        print(f"[ERROR] Error al conectar a la base de datos MySQL: {err}")
        raise err
