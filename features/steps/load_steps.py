
from behave import given
from tests.factories import ProductFactory


@given('the following products')
def step_impl(context):
    """Load sample products into the database."""
    for row in context.table:
        product = ProductFactory(
            name=row["name"],
            description=row["description"],
            category=row["category"],
            available=row["available"].lower() == "true",
            price=float(row["price"])
        )
        product.create()
