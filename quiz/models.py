from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.TextField(default="No description")
    image = models.ImageField(upload_to="quiz_images/", null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
