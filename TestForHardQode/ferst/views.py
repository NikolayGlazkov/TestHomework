from django.shortcuts import get_list_or_404,get_object_or_404,render
from django.http import JsonResponse
from .models import Product,ProductAccess  
import json 
# все продукты в виде словаря
def products_list(request):
    products = get_list_or_404(Product)
    data = [{'id': product.id, 'name': product.name, 'price': product.price, 'lessons_count': product.lesson_set.count()} for product in products]
    return render(request,"/Users/ivan/Documents/TestHomework/TestForHardQode/TestForHardQode/templates/products_list.html",{"data":data})
    # return JsonResponse(data, safe=False)
#
def user_accessible_lessons(request, product_id):
    user = request.user
    product = get_object_or_404(Product, id=product_id)
    if ProductAccess.objects.filter(user=user, product=product).exists():
        lessons = product.lesson_set.all()
        data = [{'title': lesson.title, 'video_url': lesson.video_url, 'order': lesson.order} for lesson in lessons]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'User does not have access to this product.'})