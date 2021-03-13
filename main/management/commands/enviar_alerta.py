import time 
import threading
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from apps.perdidos.models import Publicacion
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Envia mensajes de alerta de publicaciones que estan por vencer dentro de x dias'

    def add_arguments(self, parser):
        #self.stdout.write('funcion enviaralerta')
        parser.add_argument('dias_antes', nargs='+', type=int)
    
    def get_notificacion_email(self, obj, fecxdias):
        mensajes = []
        for p in obj:
            to_email = [p.id_usuario.email]
            body = render_to_string('alerta_publicacion.html',{
                'vencimiento': fecxdias,
                'usuario': p.id_usuario.username,
            }
            )
            email_message = EmailMessage(
                subject='[AmadaMascota] Renovar publicacion',
                body = body,
                from_email = settings.EMAIL_HOST_USER,
                to =to_email,
            )
            email_message.content_subtype = 'html'
            mensajes.append(email_message)
            print(p.valido_hasta, p.id_usuario, p.id_usuario.email)
            #time.sleep(5)
        return mensajes


    def handle(self, *args, **options):
        options['dias_antes'][0]
        dias_antes= options['dias_antes'][0]
        fecha_xdias = datetime.now()+timedelta(days=dias_antes)
        fecha_anter = fecha_xdias - timedelta(days=1)

        self.stdout.write(self.style.SUCCESS('Se ejecuta la funcion'))
        
        public = Publicacion.objects.all().filter(valido_hasta__gt = fecha_anter,
        valido_hasta__lte = fecha_xdias)

        connection = mail.get_connection(fail_silently=False)
        messages = self.get_notificacion_email(public, fecha_xdias)
        #print(messages)
        thread = threading.Thread(
            target = connection.send_messages,
            args= (messages,)
        )
        thread.start()

        #connection.send_messages(messages)

        self.stdout.write('enviar mensaje al autor de esta publicacion')

        #for poll_id in options['poll_ids']:
        #    try:
        #        poll = Publicacion.objects.get(pk=poll_id)
        #    except Poll.DoesNotExist:
        #        raise CommandError('Poll "%s" does not exist' % poll_id)

        #    poll.opened = False
        #    poll.save()

        #    self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))