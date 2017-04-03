from django.test import TestCase
from rest_framework import status
import json


class ApiTest(TestCase):
    fixtures = ['departments.json', 'employees.json']

    employee = {
        'name': 'Foo Bar',
        'email': 'foo@bar.com',
        'department': 'Mobile'
    }

    def test_list(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details(self):
        response = self.client.get('/employee/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = json.dumps(self.employee)

        response = self.client.post('/employee/', data, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Testa chave única email
        response = self.client.post('/employee/', data, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        data = json.dumps(self.employee)
        response = self.client.put('/employee/2/', data, 'application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete('/employee/3/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
