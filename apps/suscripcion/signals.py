from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Suscripcion
from apps.perdidos.models import Perdido
from apps.encontrados.models import Encontro
from apps.adopcion.models import Adopcion


@receiver(post_save, sender=Encontro)
def notify_new_encontrado(sender, created, **kwargs):
   if created:
      subs = Suscripcion.objects.filter(suscripcion='Encontrados')
      email_recipient_list = list(sub.id_usuario.email for sub in subs)
      try:
         send_mail(subject='New Encontrado',
                   message='¡Se registro una nueva mascota encontrada!',
                   from_email=settings.EMAIL_HOST_USER,
                   recipient_list=email_recipient_list,
                   fail_silently=False)
      except Exception as err:
         print(err)


@receiver(post_save, sender=Perdido)
def notify_new_perdido(sender, created, **kwargs):
   if created:
      subs = Suscripcion.objects.filter(suscripcion='Perdidos')
      email_recipient_list = list(sub.id_usuario.email for sub in subs)
      try:
         send_mail(subject='New Perdido',
                   message='¡Se registro una nueva mascota perdida!',
                   from_email=settings.EMAIL_HOST_USER,
                   recipient_list=email_recipient_list,
                   fail_silently=False)
      except Exception as err:
         print(err)


@receiver(post_save, sender=Adopcion)
def notify_new_adopcion(sender, created, **kwargs):
   if created:
      subs = Suscripcion.objects.filter(suscripcion='Adopcion')
      email_recipient_list = list(sub.id_usuario.email for sub in subs)
      try:
         send_mail(subject='New Adopción',
                   message='¡Se registro una nueva mascota en adopción!',
                   from_email=settings.EMAIL_HOST_USER,
                   recipient_list=email_recipient_list,
                   fail_silently=False)
      except Exception as err:
         print(err)
