from rest_framework import viewsets, permissions
from .models import Restaurant, MenuItem, Menu
from .serializers import RestaurantSerializer, MenuItemSerializer, MenuSerializer


class IsRestaurantUser(permissions.BasePermission):
    pass
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated and request.user.user_type == 'restaurant'


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsRestaurantUser]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsRestaurantUser]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsRestaurantUser]
