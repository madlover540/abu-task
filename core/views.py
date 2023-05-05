from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core import serializers
from core.models import User
from core.serializers import UserModelSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticated]

# class UserRegistrationView(viewsets.ViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#     permission_classes = []  # permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data)
#
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserModelSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = UserModelSerializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def partial_update(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


