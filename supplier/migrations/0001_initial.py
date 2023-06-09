# Generated by Django 4.2.1 on 2023-06-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(help_text='NIT', max_length=80, verbose_name='NIT')),
                ('nombre', models.CharField(help_text='Nombre', max_length=80, verbose_name='Nombre')),
                ('contacto', models.IntegerField(help_text='Teléfono o celular', null=True, verbose_name='Teléfono o celular')),
                ('ubicacion', models.CharField(help_text='Localización', max_length=300, null=True, verbose_name='Localización')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]