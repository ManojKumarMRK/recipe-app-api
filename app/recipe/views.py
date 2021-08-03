from rest_framework.serializers import Serializer
from app.core.models import User
from rest_framework import mixins,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated

from core.models import Tag

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
        
        Serializer.save(user = self.request.user)