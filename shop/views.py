from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .permissions import SenderPermission, ItemPermission, OrderPermission

from .models import Category, Item, Order
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer
from account.models import User, Profile
from django.shortcuts import render


class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [SenderPermission, ]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [SenderPermission, ]


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [ItemPermission, ]

    def get_queryset(self):
        print(self.kwargs)
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            category=get_object_or_404(Category, id=self.kwargs['category_id'])
        )


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [ItemPermission, ]


class ItemOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [OrderPermission, ]
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #
    #     serializer.save()       serializer.save(user=self.request.user)
    # def create(self, validated_data):
    #     profile = Profile.objects.get(id=self.context['request'].user.id)
    #     item = get_object_or_404(Item, id=validated_data['item_id'])
    #     if profile.is_sender != False:
    #         raise serializers.ValidationsError(
    #             {'not available': 'You cannot purchase this product with your account'})
    #     order = Order.objects.create(
    #         item=item,
    #         profile=profile
    #         )
    #     order.save()
    #     return order


    # def get(self, request, item_id):
    #     item = get_object_or_404(Item, id=item_id)
    #     order = Order.objects.create(item=item, profile=request.user.profile)
    #     data = {"message": f"Item {item_id} has been ordered by {request.user.profile}"}
    #     return Response(data, status=status.HTTP_201_CREATED)


