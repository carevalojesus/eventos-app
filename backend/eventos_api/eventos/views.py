"""
🎛️  Views — lógica del CRUD vía ViewSets.

🎯 Puntos didácticos:
   • `ModelViewSet` de rest_framework_mongoengine nos da GRATIS:
       - list()     → GET    /eventos/
       - create()   → POST   /eventos/
       - retrieve() → GET    /eventos/{id}/
       - update()   → PUT    /eventos/{id}/
       - partial_update() → PATCH /eventos/{id}/
       - destroy()  → DELETE /eventos/{id}/
   • Añadimos acciones extra con @action.
"""

from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Evento
from .serializers import EventoSerializer


class EventoViewSet(ModelViewSet):
    """CRUD completo de eventos + acciones personalizadas."""

    lookup_field = 'id'             # Usar el _id de MongoDB en la URL
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

    # 🔎 Filtro simple: permite listar solo eventos activos con ?activo=true
    def get_queryset(self):
        qs = Evento.objects.all()
        activo = self.request.query_params.get('activo')
        if activo is not None:
            qs = qs.filter(activo=(activo.lower() == 'true'))
        return qs

    # ➕ Acción extra: alternar estado activo/inactivo
    #    Ruta: POST /api/eventos/{id}/toggle/
    @action(detail=True, methods=['post'])
    def toggle(self, request, id=None):
        evento = self.get_object()
        evento.activo = not evento.activo
        evento.save()
        return Response(
            {'id': str(evento.id), 'activo': evento.activo},
            status=status.HTTP_200_OK,
        )
