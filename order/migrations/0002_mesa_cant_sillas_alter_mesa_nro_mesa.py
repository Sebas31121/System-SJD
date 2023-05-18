# Generated by Django 4.1.7 on 2023-03-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='cant_sillas',
            field=models.IntegerField(default=0, help_text='Sillas', verbose_name='Cantidad de sillas'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='nro_mesa',
            field=models.IntegerField(help_text='Mesa', verbose_name='Número de la mesa'),
        ),
    ]