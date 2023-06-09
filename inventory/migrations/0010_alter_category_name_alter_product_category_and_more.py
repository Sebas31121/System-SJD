# Generated by Django 4.1.7 on 2023-06-09 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_product_subcategory_alter_unity_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='Nombre de la categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='inventory.category', verbose_name='Categoria: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_route',
            field=models.ImageField(default='/', upload_to='product_images', verbose_name='Subir imagen: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nombre del Producto: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Precio: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Cantidad: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='unity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_unity', to='inventory.unity', verbose_name='Unidad de medida: '),
        ),
        migrations.AlterField(
            model_name='unity',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='Unidad de medida'),
        ),
    ]