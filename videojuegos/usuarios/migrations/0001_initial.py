# Generated by Django 4.0.2 on 2022-03-31 17:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='rfc_invalido', message='El RFC no tiene un formato válido', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='R.F.C.')),
                ('curp', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(code='rfc_invalido', message='El RFC no tiene un formato válido', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='C.U.R.P.')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('foto', models.ImageField(upload_to='perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
