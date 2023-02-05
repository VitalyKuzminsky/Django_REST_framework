from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase
from authapp.models import User
from todoapp.models import Project
from todoapp.views import ProjectModelViewSet, TODOModelViewSet


class TestProjectViewSet(TestCase):
    def test_get_list_projects(self):
        factory = APIRequestFactory()
        request = factory.get('/api/project/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectAPITestCase(APITestCase):
    def test_get_detail_project(self):
        user = User.objects.create(
            username='user',
            email='user@local.com',
            first_name='user',
            last_name='user'
        )
        project = Project.objects.create(name='ДЗ', repository='https://github.com')
        project.users.add(user)
        project.save()
        client = APIClient()
        response = client.get(f'/api/project/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTODOViewSet(TestCase):
    def test_get_list_todo(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todo/')
        view = TODOModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
