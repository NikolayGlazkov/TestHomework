from django.shortcuts import render,HttpResponse
from .models import Product,ProductAccess  


def products_list (request):
    products = Product.objects.all()
    
    return render(request,"/Users/ivan/Documents/TestHomework/TestForHardQode/ferst/templates/ferst/products_list.html",{"products":products})
#
def product_access_list(request):
    product_access_list = ProductAccess.objects.all()

    # Формируем HTML-разметку напрямую в функции представления
    html_output = "<h1>Product Access List</h1>"
    for entry in product_access_list:
        html_output += f"<p>{entry.user} - {entry.product}</p>"

    return HttpResponse(html_output)