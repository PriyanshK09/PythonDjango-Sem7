from django.test import TestCase
from django.urls import reverse

class CalculatorViewTests(TestCase):
    def test_add(self):
        response = self.client.get('/calc/add/2/3/')
        self.assertEqual(response.json()['result'], 5)

    def test_subtract(self):
        response = self.client.get('/calc/subtract/5/2/')
        self.assertEqual(response.json()['result'], 3)

    def test_multiply(self):
        response = self.client.get('/calc/multiply/3/4/')
        self.assertEqual(response.json()['result'], 12)

    def test_divide(self):
        response = self.client.get('/calc/divide/10/2/')
        self.assertEqual(response.json()['result'], 5)

    def test_divide_by_zero(self):
        response = self.client.get('/calc/divide/10/0/')
        self.assertIsNotNone(response.json()['error'])

    def test_invalid_operation(self):
        response = self.client.get('/calc/unknown/1/2/')
        self.assertIsNotNone(response.json()['error'])
