from django.db import models
from shared.models import CommonModel
# Create your models here.
#Creacion Tablas
class Category(models.Model):
    #Creacion de Atributos
    name=models.CharField(max_length=80,help_text="Nombre de la Categoria", unique=True)

    def __str__(self) -> str:
        return self.name
class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="fkcategory")
    name=models.CharField(max_length=80,help_text="Nombre de la Subcategoria", unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.category}"
class Product(models.Model):
    name=models.CharField("Nombre del Producto",max_length=80,help_text="Nombre del Producto")
    description=models.CharField("Descripcion",max_length=200,help_text="Descripción del producto")
    price=models.FloatField("Precio",default=0,help_text="Precio del producto")
    stock=models.IntegerField("Cantidad",default=0,help_text="En existencia")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category",blank=True,null=True,verbose_name="Categoria")
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="product_subcategory",blank=True,null=True,verbose_name="Subcategoria")

    def __str__(self) -> str:
        return f"{self.name} - {self.description} - {self.price} - {self.stock}"