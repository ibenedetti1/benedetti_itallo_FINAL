from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .modelos import Inscrito, Institucion

class FormularioInscrito(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'correo', 'telefono', 'nro_personas', 'estado', 'observacion', 'institucion_asociada']
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(FormularioInscrito, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Hacer todos los campos obligatorios excepto observación
        for field_name, field in self.fields.items():
            if field_name != 'observacion':
                field.required = True

    def clean_nro_personas(self):
        nro_personas = self.cleaned_data.get('nro_personas')
        if nro_personas < 1 or nro_personas > 30:
            raise forms.ValidationError('El número de personas debe estar entre 1 y 30')
        return nro_personas

    def clean_institucion_asociada(self):
        institucion = self.cleaned_data.get('institucion_asociada')
        if institucion and len(institucion.nombre_institucion) > 80:
            raise forms.ValidationError('El nombre de la institución no puede superar los 80 caracteres')
        return institucion


class FormularioInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre_institucion', 'correo_institucion', 'telefono_institucion', 'direccion']

    def __init__(self, *args, **kwargs):
        super(FormularioInstitucion, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
