from django.shortcuts import render,redirect
from .models import Product,ProductAccess  

def index_view(request):
    return render(request, '/Users/ivan/Documents/TestHomework/TestForHardQode/ferst/templates/ferst/index.html')

def products_list (request):
    products = Product.objects.all()
    
    return render(request,"/Users/ivan/Documents/TestHomework/TestForHardQode/ferst/templates/ferst/products_list.html",{"products":products})
#
def product_access_list(request):
    product_access_list = ProductAccess.objects.all()

    return render(request,"/Users/ivan/Documents/TestHomework/TestForHardQode/ferst/templates/ferst/user_accessible_lessons.html",{"product_access_list":product_access_list})
#