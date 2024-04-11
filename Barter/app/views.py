from django import views
from django.http import Http404
from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import   ProfileSerializer, SkillSerializer, UserSerializer, UserSkillSerializer
from .models import   Profile, Skill, UserSkill
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import SkillPermissions
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [SkillPermissions]


class ProfileDetailView(mixins.UpdateModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_profile = self.request.user.profile
        if user_profile:
            return user_profile
        else:
            # Если профиль пользователя не существует, создаем его
            Profile.objects.create(user=self.request.user)
            # И повторно пытаемся получить объект профиля
            return self.request.user.profile
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class UserSkillslView(mixins.UpdateModelMixin,  
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
