from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.OneToOneField(Skill, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.OneToOneField(Skill, on_delete=models.CASCADE, null=True,  blank=True)
    def __str__(self):
        return self.user.username