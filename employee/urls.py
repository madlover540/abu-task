
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employees')
router.register(r'menu_votes', views.MenuVoteViewSet, basename='menu_votes')
# router.register(r'top-menus', views.TopMenusViewSet, basename='top-menus')
router.register(r'menus', views.MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('top-menus/', views.TopMenusViewSet.as_view(), name='top-menus'),
]
