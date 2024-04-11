from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework import serializers
from .models import Profile, Review,  Skill
from django.db.models.signals import post_save

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
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'price')
        
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class SkillNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'price')
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_user', 'text']
        
class ReviewTextSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['user', 'text']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    #skills = SkillNameSerializer(many=True, read_only=True)
    reviews = ReviewTextSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'skills', 'reviews']
        read_only_fields = ['user']