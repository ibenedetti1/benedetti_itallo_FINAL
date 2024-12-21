from django import forms
from .modelos import Inscrito, Institucion

class FormularioInscrito(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'correo', 'telefono', 'institucion_asociada']  

    def __init__(self, *args, **kwargs):
        super(FormularioInscrito, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class FormularioInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre_institucion', 'correo_institucion', 'telefono_institucion', 'direccion']

    def __init__(self, *args, **kwargs):
        super(FormularioInstitucion, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
