from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(label='Assuntoxxx', max_length=100)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)
    email = forms.EmailField(label='E-mail', required=False)
    idade = forms.IntegerField(label='Idadexxx', required=True)
    salario = forms.DecimalField(label='Salarioxxx', required=False)    
    enviar = forms.BooleanField(label='Enviarxx', required=False)
    

class Ex003Form(forms.Form):
    PERGUNTA_CHOICES = [
        ('A', 'Paris'),
        ('B', 'Brasília'),
        ('C', 'Estocolmo'),
        ('D', 'Nova York'),
    ]

    pergunta = forms.CharField(disabled=True, label="Pergunta")
    resposta = forms.ChoiceField(choices=PERGUNTA_CHOICES, label="Resposta")


class Ex007Form(forms.Form):
    id_produto = forms.CharField(widget=forms.HiddenInput(), required=False)
    nome_produto = forms.CharField()
    qnt_produto = forms.CharField()

# class Ex006listForm(forms.Form):
#     id_produto = forms.CharField()
#     nome = forms.CharField()
#     quantidade = forms.CharField()