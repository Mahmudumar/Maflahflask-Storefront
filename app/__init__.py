from flask import Flask, render_template, redirect, url_for
import paystacker

app=Flask(__name__)


def to_naira(amount_in_kobo):
    return amount_in_kobo / 100
@app.route('/')
def index():
    products=paystacker.get_products()
    return render_template('storefront.html', products=products)

viewed_product=dict()
@app.route('/<id_>')
def get_details(id_):
    prod=paystacker.get_product(id_)
    data=prod['data']
    viewed_product.update(data)
    return redirect(url_for('product_details'))

@app.route('/product_details')
def product_details():
    return render_template('product_details.html',data=viewed_product)
