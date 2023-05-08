
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient, APITestCase

from core.models import User
from .models import Menu


class RestaurantTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            user_type=2
        )
        self.token = None
        self.test_login()


    def test_login(self):
        # Log in the user
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.data)
        self.token = response.data['access']

    def test_create_restaurant(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        restaurant_data = {
            "name": "Laziz Amarat",
            "phone_number": "+971503950224",
            "address": "dubai -jlt",
            "description": "free good restaurant",
            "is_active": True
        }

        response = self.client.post('/restaurant/restaurants/', data=restaurant_data)
        self.assertEqual(response.status_code, 201)

    def test_create_menu(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        excel_file = SimpleUploadedFile("gada_menu_hhs.xlsx", b"Dummy Excel content")
        menu_data = {
            "name": "fatoor menu",
            "excel_file": excel_file,
            "version": "1.2",
        }

        response = self.client.post('/restaurant/menus/', data=menu_data, format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_create_menu_item(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        menu = Menu.objects.create(name="Test Menu", restaurant=self.user.restaurant, version="1.0")
        image_file = SimpleUploadedFile("test_menu_image.jpeg", b"Dummy image content", content_type="image/jpeg")
        menu_item_data = {
            "name": "Fool Sudani",
            "description": "Fool with sesame oil",
            "menu": menu.id,
            "price": 5.5,
            "is_active": True,
            "image": image_file,
        }

        response = self.client.post('/restaurant/menu-items/', data=menu_item_data, format='multipart')
        self.assertEqual(response.status_code, 201)
