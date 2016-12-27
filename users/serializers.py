from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Policy, Role, RolePolicy


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.client_id')

    class Meta:
        model = Policy
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RolePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePolicy
        fields = '__all__'