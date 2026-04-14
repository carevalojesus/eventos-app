"""
🛣️  URLs raíz del proyecto.

Todas las rutas de la API se delegan a la app 'eventos' bajo el prefijo /api/.
"""

from django.urls import path, include

urlpatterns = [
    path('api/', include('eventos.urls')),
]
