from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
   class Meta:
      model = User
      fields = [
          'username',
          'email',
          'first_name',
          'last_name',
          'phone_number',
          'password1',
          'password2',
          ]
      widgets = {
          'phone_number': forms.TextInput(attrs={
              'maxlength': 18,
              'pattern': '\d*',
              }),
          }


class UpdateUserForm(forms.ModelForm):

   password = forms.CharField(max_length=15, label='Confirmar contraseña')

   class Meta:
      model = User
      fields = [
          'username',
          'email',
          'first_name',
          'last_name',
          'phone_number',
          ]
      widgets = {
          'username': forms.TextInput(attrs={'disabled': True}),
          'email': forms.TextInput(attrs={'disabled': True}),
          'phone_number': forms.TextInput(attrs={
              'maxlength': 18,
              'pattern': '\d*',
              }),
          }
