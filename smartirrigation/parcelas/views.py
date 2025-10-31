from rest_framework import viewsets, permissions, mixins, viewsets
from .models import Parcela, Sensor, Lectura
from .serializers import ParcelaSerializer, SensorSerializer, LecturaSerializer

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer
    permission_classes = [AdminOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['cultivo']
    search_fields = ['nombre', 'cultivo', 'descripcion']
    ordering_fields = ['nombre', 'superficie_ha', 'actualizado_en']
    ordering = ['nombre']

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.select_related("parcela").all()
    serializer_class = SensorSerializer
    permission_classes = [AdminOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["tipo", "estado", "parcela"]
    search_fields = ["codigo"]
    ordering_fields = ["codigo", "actualizado_en", "ultima_lectura_ts"]
    ordering = ["codigo"]


class LecturaViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = Lectura.objects.select_related("sensor").all()
    serializer_class = LecturaSerializer
    permission_classes = [AdminOrReadOnly]
    filterset_fields = ["sensor"]
    ordering_fields = ["ts", "valor"]
    ordering = ["-ts"]