from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from api.models import Item
from api.serializers.item import AllItemSerializer


# Create your views here.
class ListItemAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer


class GetItemAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer


class CreateItemAPIView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer
    permission_classes = (IsAuthenticated, )


class UpdateItemAPIView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer
    permission_classes = (IsAuthenticated, )


class DeleteItemAPIView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer
    permission_classes = (IsAuthenticated, )


class GetItemByOwner(ListAPIView):
    serializer_class = AllItemSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        return Item.objects.filter(**self.kwargs)