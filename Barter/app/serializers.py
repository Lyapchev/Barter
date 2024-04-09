from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Skill

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exist"})
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')
        
