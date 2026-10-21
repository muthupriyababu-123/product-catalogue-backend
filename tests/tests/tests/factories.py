
import factory
from factory.fuzzy import FuzzyDecimal
from service.models import Product


class ProductFactory(factory.Factory):
    """Creates fake Product objects for testing."""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    price = FuzzyDecimal(1.00, 100.00, 2)
    category = factory.Faker(
        "random_element",
        elements=["Clothing", "Food", "Electronics"]
    )
    available = factory.Faker(
        "random_element",
        elements=[True, False]
    )
