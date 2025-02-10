from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Autenticar al usuario

        # Crear una tarea de prueba
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task',
            status=False,
            due_date='2023-12-31T00:00:00Z'
        )

    def test_list_tasks(self):
        url = reverse('task-list-create')  # Nombre de la URL definida en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debería devolver 1 tarea (la que creamos en setUp)

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {
            'title': 'New Task',
            'description': 'This is a new task',
            'status': False,
            'due_date': '2023-12-31T00:00:00Z'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # Debería haber 2 tareas (la de setUp + la nueva)

    def test_retrieve_task(self):
        url = reverse('task-detail', args=[self.task.id])  # Usamos el ID de la tarea creada en setUp
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')  # Verificamos que los datos son correctos

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': 'This task has been updated',
            'status': True,
            'due_date': '2023-12-31T00:00:00Z'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()  # Actualizamos la tarea desde la base de datos
        self.assertEqual(self.task.title, 'Updated Task')  # Verificamos que el título se actualizó

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)  # Debería haber 0 tareas después de eliminar

