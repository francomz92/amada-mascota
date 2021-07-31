# Generated by Django 3.2.5 on 2021-07-30 19:00

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encontro',
            fields=[
                ('publicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apps.publicacion')),
                ('fecha_encontrado', models.DateField(help_text='¿Cuándo lo encontro?', validators=[django.core.validators.MaxValueValidator(datetime.date(2021, 7, 30), '¡La fecha no puede ser mayor a hoy!')])),
                ('cuida', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], help_text='Si está cuidando al animalito indique Si, en caso contrario indique No', max_length=2, verbose_name='En transito')),
            ],
            options={
                'verbose_name': 'Encontrado',
                'verbose_name_plural': 'Encontrados',
            },
            bases=('apps.publicacion',),
        ),
    ]
