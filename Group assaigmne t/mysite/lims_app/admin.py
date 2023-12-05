from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *

# Register your models here.
admin.site.register(reader)

@admin.register(books)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'ISBN', 'author', 'category', 'book_image']

@admin.register(mybag)
class MyBagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book']

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'mobile']

@admin.register(Orders)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'order_date', 'return_date', 'return_status']

    #to link tables in admin
    def users(self,obj):
        link=reverse('admin:app_user_change', args=[obj.book.pk])
        return format_html('<a href="{}">{}</a>',link,obj.user.name)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book']
