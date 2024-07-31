import requests
from django.test import TestCase


class CartAPITestCase(TestCase):
    def test_get_all_carts(self):
        response = requests.get('http://127.0.0.1:8000/api/shop/carts/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_cart(self):
        payload = {'user': 1}
        response = requests.post('http://127.0.0.1:8000/api/shop/carts/', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['user'], 1)

    def test_get_cart_details(self):
        response = requests.get('http://127.0.0.1:8000/api/shop/carts/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_update_cart(self):
        payload = {'user': 2}
        response = requests.put('http://127.0.0.1:8000/api/shop/carts/1/', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user'], 2)

    def test_delete_cart(self):
        response = requests.delete('http://127.0.0.1:8000/api/shop/carts/1/')
        self.assertEqual(response.status_code, 204)

    def test_create_cart_invalid_data(self):
        payload = {'user': 'invalid'}
        response = requests.post('http://127.0.0.1:8000/api/shop/carts/', json=payload)
        self.assertEqual(response.status_code, 400)

    def test_get_cart_non_existing(self):
        response = requests.get('http://127.0.0.1:8000/api/shop/carts/999/')
        self.assertEqual(response.status_code, 404)

    def test_update_cart_invalid_data(self):
        payload = {'user': 'invalid'}
        response = requests.put('http://127.0.0.1:8000/api/shop/carts/1/', json=payload)
        self.assertEqual(response.status_code, 400)

    def test_delete_cart_non_existing(self):
        response = requests.delete('http://127.0.0.1:8000/api/shop/carts/999/')
        self.assertEqual(response.status_code, 404)
