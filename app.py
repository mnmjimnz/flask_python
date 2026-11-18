from flask import Flask
from datetime import datetime
from config import Config
from controllers.animal_controller import animal_bp

def create_app():
    """Fábrica de la aplicación Flask bajo arquitectura MVC."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inyección de variables globales en plantillas Jinja2
    @app.context_processor
    def inject_globals():
        return {'now_year': datetime.now().year}

    # Registro de Controladores (Blueprints)
    app.register_blueprint(animal_bp)

    return app

# Instancia de la aplicación para servidores WSGI de producción (Render / Gunicorn)
app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("🐾 Sistema Veterinario MVC - CRUD Registro de Citas")
    print(f" Servidor iniciado en: http://127.0.0.1:{Config.PORT}")
    print(f" Conexión configurada a MySQL: {Config.DB_USER}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}")
    print("=" * 60)
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)

