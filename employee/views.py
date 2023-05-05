from .models import Employee, Vote
from .serializers import EmployeeSerializer, VoteSerializer
from rest_framework import viewsets, permissions


class IsEmployeeUser(permissions.BasePermission):
    pass
    # return after setting auth
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated and request.user.user_type == 'employee'


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsEmployeeUser]


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsEmployeeUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        app_version = self.request.META.get('HTTP_APP_VERSION', '')
        if app_version:
            queryset = queryset.filter(menu_item__version=app_version)
        return queryset
