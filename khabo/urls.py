"""khabo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from restaurants.views import RestaurantViewSet, FoodItemViewSet

api_router = SimpleRouter(trailing_slash=False)
api_router.register('restaurants', RestaurantViewSet, basename='restaurant')

restaurant_router = NestedSimpleRouter(api_router, 'restaurants', lookup='restaurant')
restaurant_router.register('food_items', FoodItemViewSet, basename='food_item')

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_router.urls)),
    path('api/v1/', include(restaurant_router.urls)),
    path('api/v1/token', obtain_auth_token),
]
