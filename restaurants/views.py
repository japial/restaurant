from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant, FoodItem
from restaurants.serializers import RestaurantSerializer, FoodItemSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().order_by('-created_at')
    serializer_class = RestaurantSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class FoodItemViewSet(ModelViewSet):
    serializer_class = FoodItemSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return FoodItem.objects.filter(restaurant_id=self.kwargs['restaurant_pk']).order_by('-created_at')


