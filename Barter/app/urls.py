from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import  ProfileDetailView, SkillView, UserSkillslView

router = DefaultRouter()
router.register(r'skills', SkillView)
router.register(r'profiles', ProfileDetailView)
router.register(r'user_skills', UserSkillslView)

urlpatterns = [
    path('', include(router.urls)),
]