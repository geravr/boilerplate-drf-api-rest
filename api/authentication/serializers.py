# Rest Framework
from rest_framework import serializers

# Models
from .models import CustomUser
from django.contrib.auth.models import Group

# Mixins
from utils.mixins.serializers import DynamicFieldsModelSerializerMixin


class CustomUserSerializer(DynamicFieldsModelSerializerMixin):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
        'is_active', 'is_staff', 'groups', 'created_at', 'updated_at', )
        read_only_fields = ('id', 'created_at', 'updated_at', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')

class WhoamiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'groups',)