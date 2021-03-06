# Generated by Django 4.0.2 on 2022-04-08 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_categoria_articulos_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleArticulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='articulos')),
                ('fotos', models.ManyToManyField(to='articulos.Articulos', verbose_name='articuloImages')),
            ],
        ),
    ]
