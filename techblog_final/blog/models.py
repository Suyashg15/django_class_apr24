from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    cont = models.TextField()
    image = models.ImageField(upload_to='blog')
    author = models.CharField(max_length=200, default="User")
    
    def __str__(self) -> str:
        return self.title