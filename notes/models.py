from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="notes")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title