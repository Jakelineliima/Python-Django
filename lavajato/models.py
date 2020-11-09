from django.db import models


class Veiculo(models.Model):
    Tipos = (
        ('C', 'Completa'),
        ('T', 'Transferencia'),
        ('P', 'Permisao')
    )
    modelo = models.CharField(max_length=30)
    placa = models.CharField(max_length=9)
    cor = models.CharField(max_length=11)
    fabricacao = models.DateField()

    def __str__(self):
        return self.placa


class Cliente(models.Model):
    nome = models.CharField(max_length=10)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.cpf


class Revisao(models.Model):
    Tipos = (
        ('C', 'Completa'),
        ('T', 'Transferencia'),
        ('P', 'Permisao')
    )


cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
Veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
Revisao = models.CharField(max_length=1, choices=Revisao, blank=False, null=False, default='M')
