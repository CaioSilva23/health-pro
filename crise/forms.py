from django import forms
from .models import Contato, AlertasCrise

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
        
            'nome': forms.TextInput(attrs={'placeholder': 'Nome...',  'class':'form-control'}),
            'celular': forms.TextInput(
                attrs={'placeholder': 'Avaliação negativa...', 'class': 'form-control'}),
                'email': forms.EmailInput(
                attrs={'placeholder': 'digite seu email', 'class': 'form-control'})
        }
        


class FormAlertasCrise(forms.ModelForm):

    class Meta:
        model = AlertasCrise
        fields = '__all__'

        widgets = {
            'nota_alerta': forms.Select(attrs={'class':'form-control text-center text-primary'}),
            'horario_acontecimento': forms.TextInput( attrs={'type': 'datetime-local', 'class':'form-control text-center text-primary'}),
            'horario_superou_crise': forms.TextInput( attrs={'type': 'datetime-local', 'class':'form-control text-center text-primary'})
        }



