import os
from pdfminer.high_level import extract_text
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from rest_framework import serializers

from .mixins import read_excel_file
from .models import Restaurant, MenuItem, Menu, ExcelFile


class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    is_active = serializers.BooleanField()

    class Meta:
        model = Restaurant
        fields = ['name', 'phone_number', 'address', 'description', 'is_active']

    def create(self, validated_data):

        restaurant = Restaurant(**validated_data)
        restaurant.user = self.context['request'].user

        restaurant.save()
        return restaurant


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'




class MenuSerializer(serializers.ModelSerializer):
    excel_file = serializers.FileField(write_only=True)
    vote_count = serializers.ReadOnlyField()

    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ('restaurant',)

    def create(self, validated_data):
        excel_file = validated_data.pop('excel_file')
        ext = os.path.splitext(excel_file)
        if ext == 'pdf':
            text = self.extract_text_from_pdf(excel_file)


        file = ExcelFile(file=excel_file)
        validated_data['excel_file'] = file
        file.save()
        restaurant = Restaurant.objects.get(user=self.context['request'].user)
        validated_data['restaurant'] = restaurant
        menu = Menu(**validated_data)
        menu.save()
        self.save_menu_items(menu, excel_file)
        return menu

    def extract_text_from_pdf(self,pdf_path):
        return extract_text(pdf_path)
    def save_menu_items(self, menu, excel_file):
        # Read data from the uploaded Excel file
        file_path = default_storage.save('temp_excel_file.xlsx', excel_file)
        excel_data = read_excel_file(file_path)

        # Save data to the MenuItem model
        for item_data in excel_data:
            MenuItem.objects.create(
                name=item_data['name'],
                description=item_data['description'],
                price=item_data['price'],
                image=item_data['image'],
                menu=menu,
                is_active=item_data['is_active'],
            )

        # Delete the uploaded file from the storage
        default_storage.delete(file_path)



