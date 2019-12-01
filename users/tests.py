from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class UserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuer',
            email = 'test@email.com',
            password = 'secret'
        )
    
    def test_signup_view_get(self):
        """
        Get a correct template for a signup
        """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_login_correct(self):
        """
        Test that the user can login with correct credentials
        """
        response = Client().login( username='testuer', password='secret')
        self.assertEqual(response, True)
    
    def test_login_fail(self):
        """
        Test that the login won't be successfull with wrong credentials
        """
        response = Client().login( username='wrongcred', password='wrongcred')
        self.assertEqual(response, False)

    def test_logout(self):
        """
        Test that the user can logout and be redirected to the homepage
        """
        Client().logout()
        response = Client().get(reverse('home'))
        self.assertNotContains(response, "Log out")

