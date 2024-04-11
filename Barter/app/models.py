from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    #reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

    
    