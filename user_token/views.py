from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import UserSerializer

class CreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"detail":"User Logout"})