from django.db import models

class LivroAutoAjuda(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    linkimg = models.ImageField(upload_to='livros/autoajuda/')
    pdf = models.FileField(upload_to='livros/autoajuda/')
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    sub_categoria = models.CharField(max_length=255, blank=True)
    estoque = models.PositiveIntegerField()
    categoria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class LivroSuspense(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    linkimg = models.ImageField(upload_to='livros/suspense/')
    pdf = models.FileField(upload_to='livros/suspense/')
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    sub_categoria = models.CharField(max_length=255, blank=True)  # Pode ser em branco
    estoque = models.PositiveIntegerField()
    categoria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class LivroRomance(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    resumo = models.TextField()
    linkimg = models.ImageField(upload_to='livros/romance/')
    pdf = models.FileField(upload_to='livros/romance/')
    nota = models.FloatField()
    sub_categoria = models.CharField(max_length=50, blank=True)
    estoque = models.IntegerField()
    categoria = models.IntegerField()


class LivroBiografia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    resumo = models.TextField()
    linkimg = models.CharField(max_length=255)
    pdf = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    sub_categoria = models.CharField(max_length=255)
    estoque = models.IntegerField()
    categoria = models.IntegerField()

    def __str__(self):
        return self.nome



