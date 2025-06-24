from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
    max_length=13,
    validators=[
        RegexValidator(
            regex=r'^(07|01)\d{8}$',
            message='Enter a valid phone number (e.g. 0712345678 or 0112345678).'
        )
    ],
    widget=forms.TextInput(attrs={
        'type': 'tel',
        'placeholder': '0712345678 or 0112345678',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
        'inputmode': 'numeric',
        'pattern': '[0-9]*'
    })
)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'placeholder': 'you@example.com (optional)',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter a strong password',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-400'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-400'
    }))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'email')


class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'placeholder': 'Email (optional)',
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Tell us about yourself...',
        'rows': 4,
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class': 'block w-full text-sm text-gray-600'
    }))

    gender = forms.ChoiceField(required=False, choices=[('', 'Select Gender')] + list(CustomUser._meta.get_field('gender').choices), widget=forms.Select(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
    }))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'bio', 'avatar', 'gender')
