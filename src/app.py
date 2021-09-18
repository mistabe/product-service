from itertools import product
from flask import Flask, json, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]

app = Flask(__name__)


@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Product with id {id} not found', 404
    return jsonify(product_list[0])

@app.route('/product', methods=['POST'])
def post_product():
    request_product = request.json

    new_id = max([product[id] for product in products]) + 1

    new_product = {
        'id': new_id,
        'name': request_product['name']
    }

    products.append(new_product)

    return jsonify(new_product), 201
