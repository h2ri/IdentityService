from rest_framework import generics
from rest_framework import permissions,viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from .models import Policy, Role, RolePolicy
from .serializers import UserSerializer, GroupSerializer, PolicySerializer, RoleSerializer, RolePolicySerializer
from .tools import get_access_token
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    permission_classes = [permissions.AllowAny,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request,*args,**kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        try:
            user = User.objects.get(username=request.data['username'])
        except Exception as e:
            return JsonResponse({'status': 'Not Authenticated'}, status=status.HTTP_200_OK)
        if user is not None:
            # return get_access_token(user, serializer)
            return get_access_token(user)
        else:
            return JsonResponse({'status': 'Not Authenticated'}, status=status.HTTP_200_OK)

class Login(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['post', ]

    def post(self,request,*args,**kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            return get_access_token(user)
        else:
            return JsonResponse({'status': 'Not Authenticated'}, status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PolicyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RolePolicyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    queryset = RolePolicy.objects.all()
    serializer_class = RolePolicySerializer

