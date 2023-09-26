from django import forms

class Ex001Form(forms.Form):
    assunto = forms.CharField(label='Assuntoxxx', max_length=100)
    idade = forms.IntegerField(label='Idadexxx', required=True)

class Ex003Form(forms.Form):
    PERGUNTA_CHOICES = [
        ('A', 'Paris'),
        ('B', 'Brasília'),
        ('C', 'Estocolmo'),
        ('D', 'Nova York'),
    ]

    pergunta = forms.CharField(disabled=True, label="Pergunta")
    resposta = forms.ChoiceField(choices=PERGUNTA_CHOICES, label="Resposta")