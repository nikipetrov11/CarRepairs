from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Потребителско име')
    password = forms.CharField(widget=forms.PasswordInput, label='Парола')