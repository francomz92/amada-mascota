from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.regex_helper import contains

# Create your models here.


class UserManager(BaseUserManager):
   def _create_user(self, username, email, first_name, last_name, phone_number, password, **kwargs):
      user = self.model(username=username,
                        email=self.normalize_email(email),
                        first_name=first_name,
                        last_name=last_name,
                        phone_number=phone_number,
                        **kwargs)
      user.set_password(password)
      user.save(using=self.db)
      return user

   def create_user(self, username, email, first_name, last_name, phone_number, password):
      return self._create_user(username, email, first_name, last_name, phone_number, password)

   def create_superuser(self, username, email, first_name, last_name, phone_number, password):
      return self._create_user(username,
                               email,
                               first_name,
                               last_name,
                               phone_number,
                               password,
                               is_staff=True,
                               is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):

   username = models.CharField(
       max_length=15,
       unique=True,
       validators=[
           MaxLengthValidator(15, '¡Máximo permitido 15 caracteres!'),
       ],
   )
   email = models.EmailField(
       max_length=30,
       unique=True,
       validators=[MaxLengthValidator(30, '¡Máximo permitido 30 caracteres!')],
   )
   first_name = models.CharField(
       max_length=25,
       validators=[MaxLengthValidator(25, '¡Máximo permitido 25 caracteres!')],
   )
   last_name = models.CharField(
       max_length=25,
       validators=[MaxLengthValidator(25, '¡Máximo permitido 25 caracteres!')],
   )
   phone_number = models.CharField(
       max_length=8,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(8, '¡Máximo permitido 8 caracteres!')],
   )
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   objects = UserManager()

   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

   def _username_validator(self):
      if self.username.find(' ') != -1:
         raise ValidationError('¡No se permiten espacios en blanco en el Username!')

   def _email_validator(self):
      if self.email.find(' ') != -1:
         raise ValidationError('¡No se permiten espacios en blanco en el Email!')

   def full_clean(self, *args, **kwargs):
      self._username_validator()
      self._email_validator()
      return super().full_clean(*args, **kwargs)

   def save(self, *args, **kwargs) -> None:
      self.full_clean()
      return super().save(*args, **kwargs)

   def __str__(self) -> str:
      return f'{self.username}'

   class Meta:
      verbose_name = 'Usuario'
      verbose_name_plural = 'Usuarios'
