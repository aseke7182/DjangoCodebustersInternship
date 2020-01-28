from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from api.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from api.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    username = token.user.username
    email = token.user.email
    response = {
        'token': token.key,
        'username': username,
        'email': email,
        'id': token.user.pk
    }
    return Response(response)


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def signup(request):
    serialized = UserSerializer(data=request.data)
    data = {}
    if serialized.is_valid():
        account = serialized.save()
        data['username'] = account.username
        data['email'] = account.email
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
