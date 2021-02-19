from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    asunto = models.CharField(max_length=300)
    mensaje = models.TextField()

    def __str__(self):
        return self.asunto