from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    sub_categoria = models.CharField(max_length=255, null=True)
    estoque = models.IntegerField()


    def __str__(self):
        return self.nome



