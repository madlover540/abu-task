from rest_framework.decorators import action
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from .models import Employee, MenuVote
from .serializers import EmployeeSerializer, MenuVoteSerializer, EmployeeMenuSerializer
from rest_framework import viewsets, permissions, generics, status
from datetime import date
from django.db.models import Q
from rest_framework.response import Response


class IsEmployeeUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'employee'


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsEmployeeUser]


class MenuVoteViewSet(viewsets.ModelViewSet):
    queryset = MenuVote.objects.all()
    serializer_class = MenuVoteSerializer
    permission_classes = [IsEmployeeUser]

    def perform_create(self, serializer):
        user = self.request.user
        # user = User.objects.last()
        employee = Employee.objects.get(user=user)
        serializer.save(employee=employee)

    def get_queryset(self):
        queryset = super().get_queryset()
        app_version = self.request.META.get('HTTP_APP_VERSION', '')
        if app_version:
            queryset = queryset.filter(menu__version=app_version)
        return queryset


class TopMenusViewSet(generics.ListAPIView):
    # queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        # top_menus = sorted(Menu.objects.all(), key=lambda menu: menu.vote_count, reverse=True)[:3]
        # # or you can modify the model to work with annotate
        # # top_menus = Menu.objects.annotate(vote_count=Count('votes')).order_by('-vote_count')[:3]
        # return top_menus

        app_version = self.request.META.get('HTTP_APP_VERSION', None)
        latest_version = '1.1'  # Set this to your latest app version
        #
        if app_version == latest_version:
            num_top_menus = 3
        else:
            num_top_menus = 1
        #
        # top_menus = Menu.objects.annotate(vote_count=Count('votes')).order_by('-vote_count')[:num_top_menus]
        # serializer = self.get_serializer(top_menus, many=True)
        # return Response(serializer.data)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = EmployeeMenuSerializer
    permission_classes = [IsEmployeeUser]

    def get_queryset(self):
        today = date.today()
        queryset = Menu.objects.filter(Q(created_at__year=today.year) &
                                       Q(created_at__month=today.month) &
                                       Q(created_at__day=today.day))
        return queryset

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        menu = self.get_object()
        employee = request.user.employee
        serializer = MenuVoteSerializer(data={'menu': menu.pk, 'employee': employee.pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Vote successful"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
