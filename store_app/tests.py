from django.test import TestCase
from django.urls import reverse

from .models import Store


class StoreTestCase(TestCase):
    def setUp(self) -> None:
        self.store = Store.objects.create(name='store_1', address='address', website='website')
        Store.objects.create(name='store_2', address='address', website='website')
        Store.objects.create(name='store_3', address='address', website='website')
        Store.objects.create(name='store_4', address='address', website='website')

    def test_fetch_all_stores(self):
        url = reverse('store:store-list')
        response = self.client.get(url)
        # Confirm response status
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Confirm number of response
        self.assertEqual(len(data), 4)

    def test_create_new_store(self):
        url = reverse('store:store-list')
        response = self.client.post(url, {
            'name': 'store_5',
            'address': 'address',
            'website': 'website',
        })
        # Confirm response status
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_store_id = data['id']
        # Confirm the saved data
        new_store = Store.objects.get(id=new_store_id)
        self.assertEqual(new_store.name, 'store_5')
        self.assertEqual(new_store.address, 'address')
        self.assertEqual(new_store.website, 'website')

    def test_fetch_specific_store(self):
        url = reverse('store:store-detail', kwargs={'pk': self.store.id})
        response = self.client.get(url)
        # Confirm response status
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Check the response data
        self.assertEqual(data['name'], self.store.name)
