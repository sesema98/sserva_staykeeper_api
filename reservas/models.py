from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    documento = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


class Reserva(models.Model):
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.PositiveIntegerField()
    cliente = models.ForeignKey(Cliente, related_name="reservas", on_delete=models.CASCADE)

    def __str__(self):
        return f"Habitación {self.numero_habitacion} - {self.fecha_ingreso} → {self.fecha_salida}"
