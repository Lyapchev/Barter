from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import  ProfileDetailView, SkillView

router = DefaultRouter()
router.register(r'skills', SkillView)
#router.register('profile/<int:pk>', ProfileDetailView.as_view(), name='profile-detail')
router.register(r'prof', ProfileDetailView)


urlpatterns = [
    path('', include(router.urls)),
]