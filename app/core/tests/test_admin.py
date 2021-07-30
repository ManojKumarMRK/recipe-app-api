from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    
        

    def test_user_list(self):
        #checks whether created user is displaying or not
        client = Client()
        admin_user = get_user_model().objects.create_superuser(
            email = 'testadmin@gmail.com',
            password = 'test@123'
        )
        client.force_login(admin_user)
        user = get_user_model().objects.create_user(
            email = 'test@gmail.com',
            password = 'test@123',
            name = 'Test name'
        )
        url = reverse('admin:core_user_changelist')
        res = client.get(url)

        self.assertContains(res,user.name)
        self.assertContains(res,user.email)
