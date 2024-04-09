from django import views
from rest_framework import viewsets, mixins, generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SkillSerializer,   UserSerializer
from .models import Skill
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import SkillPermissions
from django.contrib.auth.models import User


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [SkillPermissions]

    

    


    
