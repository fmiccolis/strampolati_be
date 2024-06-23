from rest_framework import serializers

from api.models import Item


class AllItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"