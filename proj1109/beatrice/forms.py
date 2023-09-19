from django import forms

class Ex001Form(forms.Form):
    assunto = forms.CharField(label='Assuntoxxx', max_length=100)
    idade = forms.IntegerField(label='Idadexxx', required=True)
