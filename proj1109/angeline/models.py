from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11, blank=True)
    rg = models.CharField(max_length=11, blank=True, default="999")
    last_name = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="", null=True)


    ESTADO_CIVIL_CHOICES = [
        ('CS', 'Casado'),
        ('VD', 'Viuvo'),
        ('SE', 'Separado'),
        ('UN', 'União Estável'),
        ('OU', 'Outros'),
        ('', 'Nenhum'),
    ]
    estado_civil = models.CharField(
      max_length=2,
      choices=ESTADO_CIVIL_CHOICES,
      default="",
      blank=True
    )

    def __str__(self):
        return self.nome



