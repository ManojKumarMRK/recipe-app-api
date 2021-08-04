from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Tag, Ingredient

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