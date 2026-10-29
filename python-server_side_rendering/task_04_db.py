import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append(
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        )
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv', 'sql']:
        return (
            render_template(
                'product_display.html', error="Wrong source"
            ),
            200,
        )

    try:
        if source == 'json':
            products = read_json()
        elif source == 'csv':
            products = read_csv()
        elif source == 'sql':
            products = read_sqlite()
    except (FileNotFoundError, sqlite3.Error, json.JSONDecodeError):
        return (
            render_template(
                'product_display.html', error="Database or file error"
            ),
            200,
        )

    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return (
                render_template(
                    'product_display.html', error="Product not found"
                ),
                200,
            )

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
