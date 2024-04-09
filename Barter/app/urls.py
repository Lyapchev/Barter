from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import SkillView

router = DefaultRouter()
router.register(r'skills', SkillView)



urlpatterns = [
    path('', include(router.urls)),
    path('account/register', views.UserCreate.as_view())
]