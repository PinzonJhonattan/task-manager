from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    title = models.CharField(max_length=200)                  # Título de la tarea
    description = models.TextField()                          # Descripción
    status = models.BooleanField(default=False)               # Estado (completada o no)
    due_date = models.DateTimeField()                         # Fecha límite

    def __str__(self):
        return self.title