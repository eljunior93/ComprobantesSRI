from dataclasses import field, fields
from django import forms
from .models import *

class DatosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = ['ruc', 'clave', 'origen', 'tipo', 'establecimiento', 'dia', 'mes', 'anio']

        widgets = {
            'ruc': forms.TextInput(attrs={'class':'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'establecimiento': forms.Select(attrs={'class': 'form-control'}),
            'dia': forms.Select(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'anio': forms.Select(attrs={'class': 'form-control'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['ruc'].widget.attrs.update({
    #         'class': 'form-control',
    #     })