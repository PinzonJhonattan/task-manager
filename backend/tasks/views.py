from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # Solo devuelve las tareas del usuario actual
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asigna el usuario actual a la tarea creada
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # Solo devuelve las tareas del usuario actual
        return Task.objects.filter(user=self.request.user)

