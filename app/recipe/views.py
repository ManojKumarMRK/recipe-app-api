from rest_framework.serializers import Serializer
from rest_framework import mixins,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated

from core.models import Tag, Ingredient

from recipe import serializers

class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,
                                        mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializers

    def get_queryset(self):

        return self.queryset.filter(user = self.request.user).order_by('-name')

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)


class IngViewset(viewsets.GenericViewSet,mixins.ListModelMixin,
                                mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngSerializer

    def get_queryset(self):

        return self.queryset.filter(user = self.request.user).order_by('-name')

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)