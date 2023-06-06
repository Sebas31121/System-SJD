import json
from pydantic import BaseModel
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from inventory.models import Product
from .models import Pedido
from table.models import Mesa
from order.order import Order

@login_required(login_url='/accounts/login/')
def OrderView(request):
    template_name = 'order/products_waiter.html'
    active_products = Product.objects.filter(is_active=True)
    context = {
        'title': 'SCJM-Guardar Pedido',
        'all_products': active_products
    }

    return render(request, template_name, context)

class DataOrder(BaseModel):
    id: int
    price: float
    table_number: int

@login_required(login_url='/accounts/login/')
@csrf_exempt
@require_http_methods(["POST"])
def OrderSaveView(request):
    data = json.loads(request.body.decode("utf-8"))
    data_products = data.get("products")
    data_table = data.get("table_number")
    mesa = Mesa.objects.get(nro_mesa=int(data_table))
    order = Pedido.objects.create(nro_mesa=mesa)
    productos_asignados = []

    for product in data_products:
        data_order = DataOrder(id=product["Id"], price=product["price"], table_number=int(data_table))
        products = Product.objects.filter(id=data_order.id)
        productos_asignados.extend(products)

    order.productos.set(productos_asignados)
    order.estado = 1
    order.save()

    # Verificación
    try:
        order_verify = Pedido.objects.get(id=order.id)
        success = order_verify is not None
        print(f"La orden {order.id} fue guardada correctamente: ", success)
    except Pedido.DoesNotExist:
        success = False
        print("La orden no se guardó correctamente.")

    return JsonResponse({"success": success})

@login_required(login_url='/accounts/login/')
def preView(request):
    template_name='order/waiter.html'
    producto= Product.objects.all()
    return render(request, template_name, {'productos': producto})


def order_process(request, producto_id, method):
    order = Order(request)
    producto = Product.objects.get(id=producto_id)
    getattr(order, method)(producto)
    return redirect("order:products_waiter")


@login_required(login_url='/accounts/login/')
def agregar_producto(request, producto_id):
    return order_process(request, producto_id, 'agregar')


@login_required(login_url='/accounts/login/')
def eliminar_producto(request, producto_id):
    return order_process(request, producto_id, 'eliminar_order')


@login_required(login_url='/accounts/login/')
def restar_producto(request, producto_id):
    return order_process(request, producto_id, 'restar')


@login_required(login_url='/accounts/login/')
def limpiar_producto(request, producto_id):
    return order_process(request, producto_id, 'limpiar')
