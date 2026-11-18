# 🐾 Sistema Web Veterinario - CRUD de Registro de Animales para Citas

Proyecto web desarrollado con **Python** y **Flask** bajo el patrón de arquitectura de software **MVC (Modelo - Vista - Controlador)**. Este sistema se enfoca estrictamente en el registro y gestión de citas de animales en una clínica veterinaria.

---

## 📁 Estructura del Proyecto (Patrón MVC)

```text
DESARROLLO DE SOFTWARE/
│
├── database/
│   └── schema.sql              # Script SQL para MySQL 8.4.11 LTS
│
├── models/                     # [MODELO] Lógica de negocio y consultas a MySQL
│   ├── __init__.py
│   └── animal_model.py
│
├── controllers/                # [CONTROLADOR] Recepción de peticiones HTTP y orquestación
│   ├── __init__.py
│   └── animal_controller.py
│
├── templates/                  # [VISTA] Plantillas Jinja2 / HTML con Bootstrap 5
│   ├── base.html               # Plantilla maestra / Layout
│   └── animals/
│       ├── index.html          # Vista: Listar citas registradas (Read)
│       ├── create.html         # Vista: Formulario nueva cita (Create)
│       └── edit.html           # Vista: Formulario editar cita (Update)
│
├── static/                     # Archivos estáticos (CSS, JS, imágenes)
│   └── css/
│       └── style.css
│
├── .env                        # Variables de entorno locales (credenciales DB)
├── .env.example                # Ejemplo de variables de entorno
├── app.py                      # Punto de entrada / Fábrica de Flask
├── config.py                   # Módulo de configuración
├── database.py                 # Conexión a la base de datos MySQL con PyMySQL
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación del proyecto
```

---

## 🗄️ 1. Paso 1: Ejecutar el Script en MySQL 8.4.11

El archivo con el script de base de datos se encuentra en:
📁 `database/schema.sql`

### Contenido del script:
- Crea la base de datos `veterinaria_db` con codificación `utf8mb4` compatible con MySQL 8.4.
- Crea la tabla `registro_citas_animales` con los campos necesarios para la mascota, el propietario y la cita médica.
- Inserta 3 registros de prueba iniciales para verificar la aplicación.

### Formas de ejecutar el script manualmente:

#### Opción A: Desde la consola / terminal de MySQL
```bash
mysql -u root -p < database/schema.sql
```
*(Ingresa tu contraseña cuando te sea solicitada)*

#### Opción B: Desde MySQL Workbench / DBeaver / HeidiSQL
1. Abre tu gestor de base de datos preferido conectado a tu servidor **MySQL 8.4.11**.
2. Abre el archivo `database/schema.sql` (`Archivo` -> `Abrir script SQL...`).
3. Ejecuta todo el script con el botón del rayo ⚡.

---

## ⚙️ 2. Paso 2: Configurar las Credenciales de MySQL

Abre el archivo `.env` en la raíz del proyecto y ajusta los valores de conexión de acuerdo a tu servidor MySQL:

```env
# Configuración de Base de Datos MySQL 8.4.11
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_password_aqui
DB_NAME=veterinaria_db
```

> **Nota:** Si tu usuario `root` no tiene contraseña, deja `DB_PASSWORD=` en blanco.

---

## 🚀 3. Paso 3: Ejecución de la Aplicación

El entorno virtual `venv` ya ha sido preparado en el proyecto con las dependencias instaladas (`Flask`, `PyMySQL`, `cryptography`, `python-dotenv`).

Para iniciar la aplicación:

### En Windows (PowerShell / CMD):
```powershell
# 1. Activar el entorno virtual (opcional si usas la ruta directa):
.\venv\Scripts\activate

# 2. Iniciar el servidor web:
python app.py
```

O ejecutándolo directamente con el intérprete del entorno virtual:
```powershell
.\venv\Scripts\python.exe app.py
```

### Acceder al sistema:
Abre tu navegador web e ingresa a:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## ☁️ 4. Paso 4: Despliegue en Render (render.com)

El proyecto está configurado para desplegarse fácilmente en **Render** como un **Web Service**:

### Parámetros en Render:
- **Environment:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

### Variables de Entorno en el panel de Render:
En la sección **Environment** de tu servicio en Render, agrega las siguientes variables:
- `PYTHON_VERSION`: `3.11.9`
- `SECRET_KEY`: Una cadena segura de caracteres aleatorios.
- `DB_HOST`: Host de tu base de datos MySQL en la nube (ej. TiDB, Aiven, Railway, Clever Cloud).
- `DB_PORT`: `3306` (o el puerto que te indique tu proveedor).
- `DB_USER`: Usuario de tu base de datos remota.
- `DB_PASSWORD`: Contraseña de tu base de datos remota.
- `DB_NAME`: `veterinaria_db` (o el nombre asignado en tu servicio).
- `DB_SSL`: `true` (recomendado para servicios MySQL en la nube).
*(Alternativamente, puedes configurar solo `DATABASE_URL` con el formato `mysql://usuario:password@host:puerto/nombre_bd`)*

> **Importante sobre MySQL y Render:**
> Render no ofrece MySQL administrado directamente (solo ofrece PostgreSQL). Por tanto, para producción en la nube, debes usar un servicio de MySQL remoto en la nube (como [TiDB Cloud](https://tidbcloud.com/), [Aiven](https://aiven.io/), [Railway](https://railway.app/) o [Clever Cloud](https://www.clever-cloud.com/)) y ejecutar en él el script `database/schema.sql`.

---

## 📋 Funcionalidades del CRUD

| Operación | Método HTTP | Ruta | Descripción |
|---|---|---|---|
| **Read (Listar)** | `GET` | `/animales` | Muestra la tabla de todos los animales registrados y sus citas programadas. |
| **Create (Formulario)** | `GET` | `/animales/nuevo` | Despliega el formulario para registrar un animal y programar su cita. |
| **Create (Guardar)** | `POST` | `/animales/nuevo` | Valida los datos y los inserta en la base de datos MySQL. |
| **Update (Formulario)** | `GET` | `/animales/editar/<id>` | Carga el formulario con los datos actuales del animal seleccionado. |
| **Update (Guardar)** | `POST` | `/animales/editar/<id>` | Actualiza los datos del animal y su cita en MySQL. |
| **Delete (Eliminar)** | `POST` | `/animales/eliminar/<id>` | Elimina el registro del animal con confirmación previa vía ventana modal. |

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.9+
- **Framework Web:** Flask 3.x
- **Patrón de Diseño:** MVC (Model - View - Controller)
- **Base de Datos:** MySQL 8.4.11 LTS
- **Conector DB:** `PyMySQL` + `cryptography` (compatible con la autenticación nativa y `caching_sha2_password` de MySQL 8.4)
- **Frontend / Vistas:** HTML5, CSS3, Bootstrap 5.3 y Bootstrap Icons
