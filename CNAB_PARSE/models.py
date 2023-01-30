from django.db import models


class Cnab(models.Model):
    tipo = models.CharField(max_length=1)
    data = models.DateField(max_length=10)
    valor = models.DecimalField(max_digits=256, decimal_places=2)
    cpf = models.CharField(max_length=14)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(max_length=8)
    dono_da_loja = models.CharField(max_length=14)
    nome_da_loja = models.CharField(max_length=19)
