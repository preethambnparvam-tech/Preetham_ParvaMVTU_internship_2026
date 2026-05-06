from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    terms_agreed = forms.BooleanField(required=True, label="I agree to the Terms & Conditions")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'phone_number', 
            'gender', 'usn', 'college', 'branch', 'semester', 
            'profile_picture', 'temporary_address', 'permanent_address', 
            'terms_agreed'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
