import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env si existe localmente
load_dotenv()

class Config:
    """Configuración general de la aplicación Flask para local y producción (Render)."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_super_secreta_veterinaria')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.getenv('PORT', 5000))

    # Soporte para URL completa (ej. provista por servicios cloud: mysql://user:pass@host:port/dbname)
    database_url = os.getenv('DATABASE_URL') or os.getenv('MYSQL_URL')

    if database_url:
        parsed_url = urlparse(database_url)
        DB_HOST = parsed_url.hostname or 'localhost'
        DB_PORT = parsed_url.port or 3306
        DB_USER = parsed_url.username or 'root'
        DB_PASSWORD = parsed_url.password or ''
        DB_NAME = (parsed_url.path or '/veterinaria_db').lstrip('/')
    else:
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = int(os.getenv('DB_PORT', 3306))
        DB_USER = os.getenv('DB_USER', 'root')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_NAME = os.getenv('DB_NAME', 'veterinaria_db')

    # Configuración SSL (esencial para bases de datos MySQL en la nube como Aiven, Railway, TiDB, etc.)
    DB_SSL = os.getenv('DB_SSL', 'false').lower() in ('true', '1', 't', 'yes')
