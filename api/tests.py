from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()

class AuthTests(APITestCase):
    def test_register_and_token(self):
        url = reverse('register')
        data = {'username':'tester','password':'strongpass','email':'t@example.com'}
        r = self.client.post(url, data)
        self.assertEqual(r.status_code, 201)
        token_url = reverse('token_obtain_pair')
        r2 = self.client.post(token_url, {'username':'tester','password':'strongpass'})
        self.assertEqual(r2.status_code, 200)
        self.assertIn('access', r2.data)

class TodoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('u1', password='pass1234')
        token = self.client.post(reverse('token_obtain_pair'), {'username':'u1','password':'pass1234'}).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_todo(self):
        r = self.client.post('/api/todos/', {'title':'Buy milk','description':'2 liters'})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
        t = Todo.objects.first()
        self.assertEqual(t.title, 'Buy milk')
        self.assertEqual(t.user, self.user)

    def test_list_and_detail(self):
        Todo.objects.create(user=self.user, title='a')
        Todo.objects.create(user=self.user, title='b')
        r = self.client.get('/api/todos/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 2)
        todo_id = r.data[0]['id']
        r2 = self.client.get(f'/api/todos/{todo_id}/')
        self.assertEqual(r2.status_code, 200)

    def test_update_delete(self):
        t = Todo.objects.create(user=self.user, title='to update')
        r = self.client.patch(f'/api/todos/{t.id}/', {'completed': True}, format='json')
        self.assertEqual(r.status_code, 200)
        t.refresh_from_db()
        self.assertTrue(t.completed)
        r2 = self.client.delete(f'/api/todos/{t.id}/')
        self.assertEqual(r2.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
