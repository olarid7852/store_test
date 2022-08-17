from django.test import TestCase
from django.urls import reverse

from store_app.models import Store
from .models import Order, OrderItem


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        self.store = Store.objects.create(name='store_1', address='address', website='website')
        self.order = Order.objects.create(store=self.store)
        Order.objects.create(store=self.store)
        Order.objects.create(store=self.store)
        Order.objects.create(store=self.store)
        self.second_store = Store.objects.create(name='store_2', address='address', website='website')
        Order.objects.create(store=self.second_store)

    def test_fetch_all_orders_belonging_to_a_store(self):
        url = reverse('order:order-list')
        response = self.client.get(url, {'store_id': self.store.id})
        # Confirm response status
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Confirm number of response
        self.assertEqual(len(data), 4)

    def test_fetch_all_orders(self):
        url = reverse('order:order-list')
        response = self.client.get(url)
        # Confirm response status
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Confirm number of response
        self.assertEqual(len(data), 5)

    def test_create_order(self):
        url = reverse('order:order-list')
        response = self.client.post(url, {
            'store': self.store.id,
        })
        # Confirm response status
        self.assertEqual(response.status_code, 201)
        data = response.json()
        order_id = data['id']
        new_order = Order.objects.get(id=order_id)
        self.assertEqual(new_order.store_id, self.store.id)
        self.assertEqual(new_order.status, None)


class OrderItemTestCase(TestCase):
    def setUp(self) -> None:
        self.store = Store.objects.create(name='store_1', address='address', website='website')
        self.order = Order.objects.create(store=self.store)
        self.order_item = OrderItem.objects.create(order=self.order, name='item_1')
        OrderItem.objects.create(order=self.order, name='item_2')
        OrderItem.objects.create(order=self.order, name='item_3')

        order_2 = Order.objects.create(store=self.store)
        OrderItem.objects.create(order=order_2, name='item_4')
        OrderItem.objects.create(order=order_2, name='item_5')

    def test_fetch_order_items_belonging_to_an_order(self):
        url = reverse('order:item-list', kwargs={'order_id': self.order.id})
        response = self.client.get(url)
        # Confirm response status
        self.assertEqual(response.status_code, 200)
        data = response.json()

        # Confirm number of response
        self.assertEqual(len(data), 3)

    def test_add_order_item_to_existing_order(self):
        url = reverse('order:item-list', kwargs={'order_id': self.order.id})
        response = self.client.post(url, {
            'name': 'item_6',
        })
        # Confirm response status
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_item_id = data['id']
        new_item = OrderItem.objects.get(id=new_item_id)
        self.assertEqual(new_item.order_id, self.order.id)
        self.assertEqual(new_item.name, 'item_6')

    def test_delete_order_item(self):
        url = reverse('order:item-detail', kwargs={'order_id': self.order.id, 'pk': self.order_item.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        # Confirm data deleted
        queryset = OrderItem.objects.filter(id=self.order_item.id)
        self.assertEqual(queryset.count(), 0)


    def test_update_order_item(self):
        url = reverse('order:item-detail', kwargs={'order_id': self.order.id, 'pk': self.order_item.id})
        response = self.client.patch(url, {'name': 'updated'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Confirm data updated
        order_item = OrderItem.objects.get(id=self.order_item.id)
        self.assertEqual(order_item.name, 'updated')
