from django.contrib import admin
from .models import Category,Food,FoodImage
# Register your models here.




class FoodImageInline(admin.TabularInline):
    model=FoodImage
    extra=3

class FoodAdmin(admin.ModelAdmin):
    inlines=[FoodImageInline]
# class MealAdmin(admin.ModelAdmin):
#     list_display=('name', 'price', 'category')
#     search_fields = ['name']
#     list_filter = ['category']


admin.site.register(Category)
admin.site.register(Food,FoodAdmin)
admin.site.register(FoodImage)
# admin.site.register(Meal, MealAdmin) 