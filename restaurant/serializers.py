from rest_framework import serializers
from .models import Restaurant, MenuItem, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    is_active =serializers.BooleanField()
    class Meta:
        model = Restaurant
        fields = ['name', 'phone_number', 'address', 'description', 'is_active']
    def create(self, validated_data):
        # todo debug here
        remove_this = validated_data
        restaurant = Restaurant(**validated_data)
        restaurant.user = self.context['request'].user

        restaurant.save()
        return restaurant

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'




class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    is_active = serializers.BooleanField()
    version = serializers.CharField()
    restaurant = serializers.CharField(read_only=True)
    class Meta:
        model = Menu
        fields = ['name', 'is_active', 'version', 'restaurant']
    def create(self, validated_data):
        # todo debug here
        remove_this = validated_data
        menuitem = Menu(**validated_data)
        menuitem.restaurant = Restaurant.objects.get(user=self.context['request'].user)

        menuitem.save()
        return menuitem
