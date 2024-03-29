from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_repeat = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def clean_password_repeat(self):
        data_cleaned = self.cleaned_data
        if data_cleaned['password'] != data_cleaned['password_repeat']:
            raise forms.ValidationError('Пароли должны быть одинаковыми')
        return data_cleaned['password_repeat']


class UserForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email.lower()).exclude(username=username).exists():
            raise forms.ValidationError(
                u'Пользователь с таким электронным адресом уже существует')
        return email

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', )
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
