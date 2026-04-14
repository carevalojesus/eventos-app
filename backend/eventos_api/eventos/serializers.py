"""
🔄 Serializers — convierten entre documentos MongoEngine y JSON.

🎯 Puntos didácticos:
   • Usamos `DocumentSerializer` de rest_framework_mongoengine
     (análogo a `ModelSerializer` de DRF estándar).
   • Declaramos qué campos se exponen en la API.
   • Validaciones personalizadas con `validate_<campo>`.
"""

from datetime import timezone as dt_timezone
from zoneinfo import ZoneInfo

from django.utils import timezone
from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers
from .models import Evento

LIMA_TZ = ZoneInfo('America/Lima')


class EventoSerializer(DocumentSerializer):
    """Serializa/deserializa documentos Evento."""

    class Meta:
        model = Evento
        fields = '__all__'                      # Exponer todos los campos
        read_only_fields = ('id', 'creado_en')  # No editables desde la API

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        fecha = getattr(instance, 'fecha', None)
        if fecha is not None:
            dt = fecha
            if timezone.is_naive(dt):
                dt = timezone.make_aware(dt, dt_timezone.utc)
            ret['fecha'] = self.fields['fecha'].to_representation(
                dt.astimezone(LIMA_TZ)
            )
        return ret

    # 🔍 Validación personalizada: la fecha debe ser futura al crear
    def validate_fecha(self, value):
        if timezone.is_naive(value):
            value = timezone.make_aware(value, LIMA_TZ)
        else:
            value = value.astimezone(LIMA_TZ)

        # Solo validamos al crear (no al actualizar eventos pasados)
        if self.instance is None and value < timezone.now():
            raise serializers.ValidationError(
                'La fecha del evento debe ser futura.'
            )
        return value

    # 🔍 Validación personalizada: cupo razonable
    def validate_cupo(self, value):
        if value > 10000:
            raise serializers.ValidationError(
                'El cupo no puede exceder 10,000 personas.'
            )
        return value
