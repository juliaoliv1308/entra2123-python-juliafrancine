from django.db import models
from datetime import datetime 

class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255, default="Nome Padrão")
    Sobrenome = models.CharField(max_length=255, default="Sobrenome Padrão")
    Data_nascimento = models.DateField(null=True, default=datetime.now())
    endereco = models.TextField(default="")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, default= "")

    def __str__(self):
        return f"{self.Nome} {self.Sobrenome}"




