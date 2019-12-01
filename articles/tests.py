from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class UserTests(TestCase):
    """
    TODO: Add sample post in the signUp method
    """

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'posts/posts_view.html')
    
    # def test_post_details_view(self):
    #     response =self.client.get(reverse('post_details'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'posts/post_details.html')