from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.user_serializers import UserSerializers


class UserListCreateView(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializers


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializers


