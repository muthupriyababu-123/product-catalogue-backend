
from flask import Flask, request, jsonify
from service.models import Product

app = Flask(__name__)


def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": float(product.price),
        "available": product.available,
        "category": product.category,
    }


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product_to_dict(product)), 200


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json(silent=True) or {}

    for field in ["name", "description", "price", "available", "category"]:
        if field in data:
            setattr(product, field, data[field])

    product.update()
    return jsonify(product_to_dict(product)), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    product.delete()
    return "", 204


@app.route("/products", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available is not None:
        products = Product.find_by_availability(
            available.lower() == "true"
        )
    else:
        products = Product.all()

    return jsonify([product_to_dict(p) for p in products]), 200
