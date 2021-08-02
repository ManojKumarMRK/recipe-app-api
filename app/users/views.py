from rest_framework import generics

from users.serializers_user import User_serializers



class CreateUserView(generics.CreateAPIView):
    #create a new user in  a system
    serializer_class = User_serializers

