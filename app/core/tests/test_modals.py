from django.test import TestCase
from django.contrib.auth import get_user_model

class ModalTests(TestCase):

    def test_create_use_with_creds(self):

        #function to check the user is created successfully
        email = 'test@gmail.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_email_normalize(self):

        #function to check whether the email normalized or not
        email = 'test@GMail.com'
        user = get_user_model().objects.create_user(
            email = email,
            password = 'test@123'
        )
        self.assertEqual(user.email,email.lower())

    def test_check_superuser(self):

        #function to check superuser created successfully
        user = get_user_model().objects.create_superuser(
            email = 'test@gmail.com',
            password = 'test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_isvalid_email(self):

        #function to check wether email is not null
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test@123')
