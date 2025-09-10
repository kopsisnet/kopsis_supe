from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            base_class = (
                "w-full px-3 py-2 border rounded shadow-sm focus:outline-none "
                "focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            )
            if self.errors.get(field_name):
                base_class += " border-red-500"
            else:
                base_class += " border-gray-300"
            field.widget.attrs['class'] = base_class
