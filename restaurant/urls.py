from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# from .views import MenuUploadExcelViewSet

# menu_upload_excel = MenuUploadExcelViewSet.as_view()

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menu-items', views.MenuItemViewSet)
router.register(r'menus', views.MenuViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('menu-upload/', menu_upload_excel, name='menu-upload'),
]
