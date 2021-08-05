from rest_framework.serializers import Serializer
from rest_framework import mixins,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated

from core.models import Tag, Ingredient, Recipe

from recipe import serializers

class RecipeCommonAttr(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        return self.queryset.filter(user = self.request.user).order_by('-name')

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class TagViewSet(RecipeCommonAttr):

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializers


class IngViewset(RecipeCommonAttr):

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngSerializer


class RecipeViewset(RecipeCommonAttr):

    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def get_serializer_class(self):
    
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class