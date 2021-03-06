from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from rest_framework import serializers

class User_serializers(serializers.ModelSerializer):
    #serializers for user
    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'min_length' : 5
            }
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class Auth_token_serializers(serializers.Serializer):
    #serializers for auth token
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type' : 'password'}
    )
    def validate(self,attrs):

        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password

        )
        if not user:
            msg = _("Unable to autherticate")
            raise serializers.ValidationError(msg,code = 'authentication')

        attrs['user'] = user
        return attrs
