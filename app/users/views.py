from users.serializers_user import Auth_token_serializers
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializers_user import User_serializers
from rest_framework.settings import api_settings



class CreateUserView(generics.CreateAPIView):
    #create a new user in  a system
    serializer_class = User_serializers

class CreateTokenView(ObtainAuthToken):
    #create a new token if credentials are correct
    serializer_class = Auth_token_serializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    #modify user data
    serializer_class = User_serializers
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user