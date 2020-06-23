from rest_framework import serializers

from restaurants.models import Restaurant, FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name')
        read_only_field = ('id',)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone')
        read_only_field = ('id',)
