from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # These are the fields we want to turn into JSON
        fields = ['id', 'title', 'description', 'is_completed', 'created_at']