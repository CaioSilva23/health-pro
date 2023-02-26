from django import forms
from .models import AvaliacaoDiaria



class FormAvaliacaoDiaria(forms.ModelForm):
    class Meta:
        model = AvaliacaoDiaria
        fields = '__all__'
        widgets = {
            'rating': forms.Select(attrs={'class':'form-control text-center text-primary'}),
            'anotacao_positiva': forms.Textarea(attrs={'placeholder': 'Avaliação positiva...','rows':3, 'class': 'form-control'}),
            'anotacao_negativa': forms.Textarea(
                attrs={'placeholder': 'Avaliação negativa...', 'rows':3, 'class': 'form-control'}),
        }
        