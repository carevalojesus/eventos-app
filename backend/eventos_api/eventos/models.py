"""
📄 Modelo de datos — Evento

🎯 Puntos didácticos:
   • Usamos `mongoengine.Document` en vez de `django.db.models.Model`.
   • Cada campo es un `Field` de MongoEngine (similar al ORM de Django).
   • MongoDB NO necesita migraciones: los documentos se crean dinámicamente.
   • `meta` permite configurar la colección, índices, etc.
"""

from mongoengine import Document, StringField, DateTimeField, IntField, BooleanField
from datetime import datetime


class Evento(Document):
    """Representa un evento en la base de datos MongoDB."""

    titulo = StringField(
        required=True,
        max_length=200,
        help_text='Nombre del evento'
    )
    descripcion = StringField(
        required=True,
        help_text='Descripción detallada del evento'
    )
    fecha = DateTimeField(
        required=True,
        help_text='Fecha y hora del evento (ISO 8601)'
    )
    lugar = StringField(
        required=True,
        max_length=200,
        help_text='Ubicación del evento'
    )
    cupo = IntField(
        required=True,
        min_value=1,
        help_text='Número máximo de asistentes'
    )
    activo = BooleanField(
        default=True,
        help_text='Indica si el evento está vigente'
    )
    creado_en = DateTimeField(
        default=datetime.utcnow,
        help_text='Timestamp de creación (auto)'
    )

    # ⚙️ Configuración del documento
    meta = {
        'collection': 'eventos',          # Nombre de la colección en MongoDB
        'ordering': ['-fecha'],           # Orden por defecto: más recientes primero
        'indexes': [
            'titulo',                     # Índice para búsquedas por título
            '-fecha',                     # Índice descendente por fecha
        ],
    }

    def __str__(self):
        return f'{self.titulo} ({self.fecha:%d/%m/%Y})'
