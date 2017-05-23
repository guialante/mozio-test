# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import json

from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from mozio_test.providers.models import Provider, ServiceArea


class TestProviderAPIView(APITestCase):

    def setUp(self):
        url = reverse('providers:provider-list')
        self.data = {
            'name': 'Uber', 'email': 'support@uber.com', 'phone_number': '890456789', 'language': 'English',
            'currency': 'USD'
        }
        self.response = self.client.post(url, self.data, format='json')

    def test_create_view(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        instance = Provider.objects.get()
        url = reverse('providers:provider-detail', kwargs={'pk': instance.pk})
        self.url = url
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, instance)

    def test_partial_update_view(self):
        instance = Provider.objects.get()
        url = reverse('providers:provider-detail', kwargs={'pk': instance.pk})
        data = {'name': 'Peter Peres'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_view(self):
        instance = Provider.objects.get()
        url = reverse('providers:provider-detail', kwargs={'pk': instance.pk})
        data = {'name': 'Peter Peres', 'email': 'peter@gmail.com', 'phone_number': '1234567890'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_view(self):
        instance = Provider.objects.get()
        url = reverse('providers:provider-detail', kwargs={'pk': instance.pk})
        response = self.client.delete(url, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestServiceAreaAPIView(APITestCase):

    def setUp(self):
        self.provider = Provider.objects.create(**{
            'name': 'John Doe', 'email': 'jonh@gmail.com', 'phone_number': '890456789', 'language': 'English',
            'currency': 'USD'
        })
        self.coords = {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -122.47266769409178,
                        37.78441844686463
                    ],
                    [
                        -122.47202396392821,
                        37.780721409443764
                    ],
                    [
                        -122.45897769927977,
                        37.78126410541595
                    ],
                    [
                        -122.45919227600098,
                        37.78496111569183
                    ],
                    [
                        -122.47266769409178,
                        37.78441844686463
                    ]
                ]
            ]
        }
        url = reverse('providers:servicearea-list')
        self.data = {
            'name': 'San Francisco Area', 'price': 25.0, 'service_area_provider': self.provider.pk,
            'area': self.coords
        }
        self.response = self.client.post(url, self.data, format='json')

    def test_create_view(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_view(self):
        instance = ServiceArea.objects.get()
        url = reverse('providers:servicearea-detail', kwargs={'pk': instance.pk})
        self.url = url
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, instance)

    def test_partial_update_view(self):
        instance = ServiceArea.objects.get()
        url = reverse('providers:servicearea-detail', kwargs={'pk': instance.pk})
        data = {'name': 'New York Central Park'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_view(self):
        instance = ServiceArea.objects.get()
        url = reverse('providers:servicearea-detail', kwargs={'pk': instance.pk})
        data = {'price': 50.0, 'service_area_provider': self.provider.pk, 'name': 'New York Bay Area', 'area': self.coords}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_view(self):
        instance = ServiceArea.objects.get()
        url = reverse('providers:servicearea-detail', kwargs={'pk': instance.pk})
        response = self.client.delete(url, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
