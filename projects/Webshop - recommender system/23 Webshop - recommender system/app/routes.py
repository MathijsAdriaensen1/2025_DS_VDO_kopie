from flask import render_template
from app import app
from app.db import get_connection
from app.models import Product

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/recommender')
def recommender():
    return "Dit is de recommender page!"


@app.route('/products')
def products():
    # get products from db
    my_products = Product.get_all()
    return render_template("products.html", products=my_products)
