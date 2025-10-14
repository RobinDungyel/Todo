from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data.get('email'),
                                        password=validated_data['password'])
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed','created_at','updated_at')
        read_only_fields = ('id','created_at','updated_at')
