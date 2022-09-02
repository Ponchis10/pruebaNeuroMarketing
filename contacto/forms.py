from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='nombre', required=True)
    email = forms.EmailField(label='email', required=True)
    asunto = forms.CharField(label='asunto', required=True)
    contenido = forms.CharField(label='contenido', widget=forms.Textarea)