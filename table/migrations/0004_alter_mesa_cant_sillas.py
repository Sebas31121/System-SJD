# Generated by Django 4.2.1 on 2023-06-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_alter_mesa_nro_mesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='cant_sillas',
            field=models.IntegerField(default=4, help_text='Sillas', verbose_name='Cantidad de sillas'),
        ),
    ]
