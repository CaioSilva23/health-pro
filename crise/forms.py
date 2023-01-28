from django import forms
from .models import Contato, AlertasCrise

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        
class DateInput(forms.DateInput):
    input_type = 'date'


class FormAlertasCrise(forms.ModelForm):
    class Meta:
        model = AlertasCrise
        fields = '__all__'

        widgets = {
            'horario_acontecimento': DateInput(),
            'horario_superou_crise': DateInput()
        }



