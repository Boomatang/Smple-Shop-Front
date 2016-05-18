from flask import render_template
from . import main


@main.route('/')
def index():
    values = range(0, 8)

    return render_template("main/index.html", list=values)


@main.route("/products")
def products():
    values = range(0, 25)

    return render_template("main/products.html", list=values)


@main.route("/contact")
def contact():
    return render_template("main/contact.html")


@main.route("/products/<item>")
def product_view(item):
    return render_template("main/product-view.html")


@main.route("/cart")
def cart():
    values = range(0, 4)
    return render_template("main/cart.html", values=values)