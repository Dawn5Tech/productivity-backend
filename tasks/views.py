from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    # These two lines replace all the GET/POST functions!,it handles List, Create, Retrieve, Update, and Delete
    #queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # New line
    
    # This replaces 'queryset = Task.objects.all()'
    def get_queryset(self):
        # We only return tasks where the owner is the person currently logged in
        return Task.objects.filter(owner=self.request.user)
    
    # This ensures that when a task is created, the 'owner' is set automatically
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)