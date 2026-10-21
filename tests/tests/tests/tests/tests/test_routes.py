
import unittest
import json
from service.routes import app
from service.models import db
from tests.factories import ProductFactory


class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_product(self):
        product = ProductFactory()
        product.create()
        response = self.client.get(f"/products/{product.id}")
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = ProductFactory()
        product.create()
        response = self.client.put(
            f"/products/{product.id}",
            data=json.dumps({"name": "Updated Product"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        product = ProductFactory()
        product.create()
        response = self.client.delete(f"/products/{product.id}")
        self.assertIn(response.status_code, [200, 204])

    def test_list_all_products(self):
        for product in ProductFactory.build_batch(3):
            product.create()
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

    def test_list_products_by_name(self):
        product = ProductFactory(name="Hat")
        product.create()
        response = self.client.get("/products?name=Hat")
        self.assertEqual(response.status_code, 200)

    def test_list_products_by_category(self):
        product = ProductFactory(category="Food")
        product.create()
        response = self.client.get("/products?category=Food")
        self.assertEqual(response.status_code, 200)

    def test_list_products_by_availability(self):
        product = ProductFactory(available=True)
        product.create()
        response = self.client.get("/products?available=true")
        self.assertEqual(response.status_code, 200)
