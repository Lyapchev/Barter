from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer, ReviewSerializer, SkillSerializer, UserSerializer
from .models import Profile, Review, Skill
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import SkillPermissions, IsOwnerOrReadOnly
from django.contrib.auth.models import User


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [SkillPermissions]

    
class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
         serializer.save(user=self.request.user)
    
class ProfileDetailView(mixins.UpdateModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
         serializer.save(user=self.request.user)
         
    