from django.contrib import admin
from .models import Product, ProductAccess, Lesson, Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_datetime', 'price', 'creator') 
    search_fields = ('name', 'creator__username')  

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'video_url')
    list_filter = ('product',)  
    search_fields = ('title',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    search_fields = ('name', 'product__name')
    filter_horizontal = ('members',)  # Используйте 'members' вместо 'students'

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAccess)  
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Group, GroupAdmin)
