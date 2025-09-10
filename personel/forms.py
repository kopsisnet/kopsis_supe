from django import forms
from .models import Personel

class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        fields = '__all__'
        widgets = {
            'dogum_tarihi': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
