from rest_framework.serializers import ModelSerializer
from .models import User, Profile


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'programming_language', 'photo']


class ProfileUserSerializer(ModelSerializer):
    user = UserViewSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'points', 'win_count', 'lose_count']
