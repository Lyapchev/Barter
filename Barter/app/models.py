from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    review_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    

    
    