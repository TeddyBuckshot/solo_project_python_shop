from flask import Flask, render_template, Blueprint, request, redirect
import repositories.brand_repository as brand_repository

brand_blueprint = Blueprint("brands", __name__)

@brand_blueprint.route("/brands")
def brands():
    brands = brand_repository.select_all()
    return render_template("brands/view-brands.html", brands = brands)

@brand_blueprint.route("/brands/<id>")
def show(id):
    brand = brand_repository.select(id)
    keyboards = brand_repository.get_all_keyboards(brand)
    return render_template("brands/view-products.html", brand=brand, keyboards=keyboards)
