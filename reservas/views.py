from rest_framework import viewsets, filters
from .models import Cliente, Reserva
from .serializers import ClienteSerializer, ReservaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["numero_habitacion", "cliente__nombre"]
