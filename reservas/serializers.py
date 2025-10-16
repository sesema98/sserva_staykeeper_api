from rest_framework import serializers
from .models import Cliente, Reserva

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'documento']

class ReservaSerializer(serializers.ModelSerializer):
     # ⚙️ PERSONALIZACIÓN (+1): aca estoy incluyendo el nombre del cliente en la representación de la reserva
     # para que sea más fácil identificar a quién pertenece cada reserva sin hacer una consulta adicional.
    cliente_nombre = serializers.CharField(source="cliente.nombre", read_only=True)
    class Meta:
        model = Reserva
        fields = ["id", "fecha_ingreso", "fecha_salida", "numero_habitacion", "cliente", "cliente_nombre"]