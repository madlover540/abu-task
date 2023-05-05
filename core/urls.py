from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UserRegistrationView, UserLoginView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
]
