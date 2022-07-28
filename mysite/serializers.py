import django


from django.contrib.auth.models import User,Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

