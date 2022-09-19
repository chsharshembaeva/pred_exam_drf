from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import User, Profile
from .serializers import RegisterSerializer, ProfileSerializer


class SenderRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=True)


class BuyerRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=False)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAdminUser, ]

