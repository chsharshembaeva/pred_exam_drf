from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .permissions import SenderPermission, ItemPermission, OrderPermission

from .models import Category, Item, Order
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer



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


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [OrderPermission, ]

    def get_queryset(self):
        print(self.kwargs)
        return self.queryset.filter(item_id=self.kwargs['item_id'])

    def perform_create(self, serializer):
        serializer.save(
            profile=self.request.user.profile,
            item=get_object_or_404(Item, id=self.kwargs['item_id'])
        )

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


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [OrderPermission, ]



