
import unittest
from service.models import Product, db
from tests.factories import ProductFactory


class TestProduct(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_read_a_product(self):
        product = ProductFactory()
        product.create()
        found = Product.find(product.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.id, product.id)

    def test_update_a_product(self):
        product = ProductFactory()
        product.create()
        product.name = "Updated Product"
        product.update()
        found = Product.find(product.id)
        self.assertEqual(found.name, "Updated Product")

    def test_delete_a_product(self):
        product = ProductFactory()
        product.create()
        product_id = product.id
        product.delete()
        self.assertIsNone(Product.find(product_id))

    def test_list_all_products(self):
        products = ProductFactory.build_batch(5)
        for product in products:
            product.create()
        found = Product.all()
        self.assertEqual(found.count(), 5)

    def test_find_by_name(self):
        product = ProductFactory(name="Hat")
        product.create()
        found = Product.find_by_name("Hat")
        self.assertTrue(any(p.name == "Hat" for p in found))

    def test_find_by_category(self):
        product = ProductFactory(category="Food")
        product.create()
        found = Product.find_by_category("Food")
        self.assertTrue(any(p.category == "Food" for p in found))

    def test_find_by_availability(self):
        product = ProductFactory(available=True)
        product.create()
        found = Product.find_by_availability(True)
        self.assertTrue(any(p.available is True for p in found))
