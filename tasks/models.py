from django.db import models
from django.contrib.auth.models import User # Import the built-in User

# Create your models here.
class Task(models.Model):
    # This links the task to a specific user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    
    # CharField is for short text (like a title)
    title = models.CharField(max_length=200)
    
    # TextField is for long text (like a description)
    description = models.TextField(blank=True)
    
    # BooleanField is a True/False switch
    is_completed = models.BooleanField(default=False)
    
    # DateTimeField automatically tracks when the task was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title