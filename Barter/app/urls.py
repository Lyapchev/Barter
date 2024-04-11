from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ProfileDetailView, ReviewView, SkillView

router = DefaultRouter()
router.register(r'skills', SkillView)
router.register(r'profiles', ProfileDetailView)
router.register(r'reviews', ReviewView)


urlpatterns = [
    path('', include(router.urls)),
]