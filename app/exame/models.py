from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.TextField(unique=True)
    idade = models.IntegerField()
    endereco = models.TextField()


class Exame(models.Model):
    nome_profissional = models.TextField()
    data_exame = models.DateTimeField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
