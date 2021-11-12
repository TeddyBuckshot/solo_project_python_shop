from flask import Flask, render_template, Blueprint, request, redirect
from models.brand import Brand
import repositories.brand_repository as brand_repository

brand_blueprint = Blueprint("brands", __name__)

@brand_blueprint.route("/brands")
def show_brands():
    brands = brand_repository.select_all()
    return render_template("brands/view-brands.html", brands = brands)

@brand_blueprint.route("/brands/new")
def new_brand():
    new_brand = brand_repository.select_all()
    return render_template("brands/new-brand.html", new_brand=new_brand)

@brand_blueprint.route("/brands", methods=["POST"])
def create_brand():
    name = request.form["name"]
    origin = request.form["origin"]
    new_brand = Brand(name, origin)
    brand_repository.save(new_brand)
    return redirect("/brands")

@brand_blueprint.route("/brands/<id>/edit")
def edit_brand(id):
    brand = brand_repository.select(id)
    return render_template('brands/edit-brand.html', brand=brand)

@brand_blueprint.route("/brands/<id>", methods=["POST"])
def update_brand(id):
    name = request.form["name"]
    origin = request.form["origin"]
    brand = brand_repository.select(id)
    brand_active = None
    if "active" in request.form:
        brand_active = False 
    elif "inactive" in request.form:
        brand_active = True
    elif brand_active is None:
        brand_active = brand_repository.is_brand_active(brand)

    updated_brand = Brand(name, origin, brand_active, id)
    brand_repository.update(updated_brand)
    return redirect("/brands")