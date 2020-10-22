# Rest Framework
from rest_framework import serializers

# Models
from .models import CustomUser
from django.contrib.auth.models import Group, Permission

# Mixins
from utils.mixins.serializers import DynamicFieldsModelSerializerMixin


class CustomUserSerializer(DynamicFieldsModelSerializerMixin):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name'
     )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
        'is_active', 'is_staff', 'groups', 'created_at', 'updated_at', )
        read_only_fields = ('id', 'created_at', 'updated_at', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        for group in groups:
            user.groups.add(group)
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SlugRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        slug_field='name'
     )
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class WhoamiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'groups',)
