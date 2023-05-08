from rest_framework import serializers

from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from .models import Employee, MenuVote


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    votes = serializers.CharField(read_only=True)
    job_title = serializers.CharField()
    department = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('id', 'user', 'votes', 'job_title', 'department', 'phone_number', 'address')

    def create(self, validated_data):
        employee = Employee(**validated_data)
        employee.user = self.context['request'].user

        employee.save()
        return employee



class MenuVoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuVote
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.fields]  # or u can write the fields name manually

class EmployeeMenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = [f.name for f in model._meta.fields]
