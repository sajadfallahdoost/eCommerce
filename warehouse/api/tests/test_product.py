from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from warehouse.models.product import Product  # adjust import according to your project structure
from warehouse.api.serializers import ProductSerializer  # adjust import according to your project structure


class ProductListCreateAPITest(APITestCase):

    def setUp(self):
        # Create a sample product to test GET request
        self.product = Product.objects.create(name="Test Product", price=100.00)
        self.url = reverse('product-list-create')  # Ensure this is the correct URL name for your view

    def test_get_product_list(self):
        # Test the GET request to list products
        response = self.client.get(self.url)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        # Test the POST request to create a new product
        data = {
            "title": "ball no 2",
            "slug": "ball-no-2",
            "subtitle": "Initially composing light-hearted and irreverent works, he also wrote serious, sombre and religious pieces beginning in the 1930s.",
            "can_review": True,
            "is_active": True,
            "suggested_products": [732]
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['slug'], data['slug'])
        self.assertTrue(Product.objects.filter(title='"ball no 2').exists())

    def test_create_product_invalid_data(self):
        # Test the POST request with invalid data
        data = {
            "title": "",
            "slug": "111",
            "subtitle": "Initially composing light-hearted and irreverent works, he also wrote serious, sombre and religious pieces beginning in the 1930s.",
            "can_review": True,
            "is_active": True,
            "suggested_products": [0]
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertIn('slug', response.data)
