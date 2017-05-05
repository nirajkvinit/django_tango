from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
#/home/nirajkvinit/code/django/tango_with_django_project/rango/admin.py
