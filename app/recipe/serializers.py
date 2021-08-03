from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from core.models import Tag

class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_field = ('id')