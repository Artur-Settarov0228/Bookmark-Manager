from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100 ,unique=True)

    def __str__(self):
        return self.name
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmark')

    title = models.CharField(max_length= 60)
    description = models.TextField( blank=True , null=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='bookmark')

    def __str__(self):
        return self.title    
        
  
