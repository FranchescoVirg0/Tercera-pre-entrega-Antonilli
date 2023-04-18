from django import forms
from AppCpder.models import *
class formularioConsorcista(forms.ModelForm):
    class Meta:
        model = Consorcista
        fields = '__all__'

class formularioAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class formularioExpensa(forms.ModelForm):
    class Meta:
        model = Expensa
        fields = '__all__'
        widgets = {"fecha_venc" : forms.DateInput(attrs={'type': 'date'})}