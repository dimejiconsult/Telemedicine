from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'email', 'first_name', 'last_name']