"""
⚙️  Configuración principal del proyecto Django.

🎯 Puntos didácticos clave:
   1. Usamos MongoEngine (ODM) en vez del ORM de Django, porque MongoDB es NoSQL.
   2. DATABASES queda vacío: Django no usará SQL para nuestros modelos de negocio.
   3. mongoengine.connect() establece la conexión con MongoDB Atlas.
   4. Las variables sensibles se leen desde .env (nunca se suben al repo).
"""

from pathlib import Path
from decouple import config
import mongoengine

# 📁 Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Seguridad
SECRET_KEY = config('SECRET_KEY', default='dev-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['*']  # Para desarrollo. En producción: lista explícita.

# 📦 Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'rest_framework_mongoengine',
    'corsheaders',

    # Nuestras apps
    'eventos',
]

# 🧱 Middleware (orden importante: CORS debe ir arriba)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'eventos_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    },
]

WSGI_APPLICATION = 'eventos_api.wsgi.application'

# 🗄️  Django SQL "vacío": no usamos la DB relacional para nuestros modelos.
#     MongoEngine se encarga de hablar con MongoDB Atlas.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Solo para tablas internas de Django
    }
}

# 🍃 Conexión a MongoDB Atlas usando MongoEngine
#    Esta es LA línea mágica que conecta Django con MongoDB.
mongoengine.connect(
    db=config('MONGODB_DB', default='eventos_db'),
    host=config('MONGODB_URI'),
    alias='default',
)

# 🌐 CORS: permitir que nuestro frontend Astro consuma la API
CORS_ALLOWED_ORIGINS = [
    config('CORS_ORIGIN', default='http://localhost:4321'),
]

# 🌎 Internacionalización
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# 📂 Archivos estáticos
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🛠️  Configuración de Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # Didáctico: UI en navegador
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
