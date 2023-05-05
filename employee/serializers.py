from rest_framework import serializers
from .models import Employee, Vote


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



class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
