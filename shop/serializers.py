from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from account.models import Profile
from .models import Category, Item, Order


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ['profile', 'category']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['profile', 'item']

    #
    # def create(self, validated_data):
    #     profile = Profile.objects.get(id=self.context['request'].user.id)
    #     item = get_object_or_404(Item, id=validated_data['item_id'])
    #     order = Order.objects.create(
    #         item=item,
    #         profile=profile
    #         )
    #     order.save()
    #     return order

