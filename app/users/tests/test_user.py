from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('users:create')



class PublicUserApiTest(TestCase):

    

    def test_create_user_success(self):

        payload = {
            'email' : 'ab@abd.com',
            'password' : 'pass@test1',
            'name' : 'test1 name'
        }
        client = APIClient()

        res = client.post('http://127.0.0.1:8000/api/users/create/',payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.create_user(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)

