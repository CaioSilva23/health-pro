from django import forms
from .models import Contato, AlertasCrise

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
        
            'nome': forms.TextInput(attrs={'placeholder': 'Nome...', 'class': 'form-control'}),
            'celular': forms.TextInput(
                attrs={'placeholder': 'Avaliação negativa...', 'class': 'form-control'}),
                'email': forms.EmailInput(
                attrs={'placeholder': 'digite seu email', 'class': 'form-control'})
        }
        
        
class DateInput(forms.DateInput):
    input_type = 'date'


class FormAlertasCrise(forms.ModelForm):
    class Meta:
        model = AlertasCrise
        fields = '__all__'

        widgets = {
            'horario_acontecimento': DateInput( attrs={'type': 'date'}, format='%Y-%m-%d'),
            'horario_superou_crise': DateInput( attrs={'type': 'date'}, format='%Y-%m-%d')
        }



