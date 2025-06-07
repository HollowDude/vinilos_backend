from datetime import date
from django.db import models
from .producto import Producto

class Reporte_Abastecimiento(models.Model):
    ESTADO = [
        ('Entregado','entregado'),
        ('Pedido','pedido')
    ]


    nombre = models.CharField(max_length=30)
    estado = models.CharField(max_length=255, choices=ESTADO, default='Pedido')
    fecha_pedido = models.DateField(default=date.today)
    fecha_llegada = models.DateField(null=True, blank=True)
    costoTot = models.DecimalField(max_digits=15, decimal_places=2, default=1.00, null=True, blank=True)
    

    class Meta:
        verbose_name = "Reporte_Abastecimiento"
        verbose_name_plural = "Reportes_Abastecimiento"

class ItemPedido(models.Model): 
    pedido = models.ForeignKey(Reporte_Abastecimiento, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)