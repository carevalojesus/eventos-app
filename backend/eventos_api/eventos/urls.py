"""
🛣️  Rutas de la app eventos.

Usamos DefaultRouter para generar todas las rutas REST automáticamente.
"""

from rest_framework.routers import DefaultRouter
from .views import EventoViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet, basename='evento')

# DRF genera automáticamente:
#   GET    /api/eventos/
#   POST   /api/eventos/
#   GET    /api/eventos/{id}/
#   PUT    /api/eventos/{id}/
#   PATCH  /api/eventos/{id}/
#   DELETE /api/eventos/{id}/
#   POST   /api/eventos/{id}/toggle/
urlpatterns = router.urls
