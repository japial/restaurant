from django.contrib import admin

from restaurants.models import Restaurant, FoodItem


class FoodItemInline(admin.StackedInline):
    model = FoodItem
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    inlines = [FoodItemInline]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name']
