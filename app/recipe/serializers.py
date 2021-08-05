from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import ReadOnlyField

from core.models import Tag, Ingredient, Recipe

class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_field = ('id')

class IngSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_field = ('id')

class RecipeSerializer(serializers.ModelSerializer):

    Ingredients = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('name','user','duration_mins','cost','tags',
                        'Ingredients','servings','link')
        ReadOnlyField = ('id')

class RecipeDetailSerializer(RecipeSerializer):

    Ingredients = IngSerializer(many=True, read_only = True)
    tags = TagSerializers(many=True, read_only = True)