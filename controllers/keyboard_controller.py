from flask import Flask, render_template, Blueprint, request, redirect
from models.keyboard import Keyboard
import repositories.keyboard_repository as keyboard_repository
import repositories.brand_repository as brand_repository


keyboard_blueprint = Blueprint("keyboards", __name__)


@keyboard_blueprint.route("/keyboards")
def show_keyboards():
    keyboards = keyboard_repository.select_all()
    return render_template("keyboards/view-keyboards.html", keyboards=keyboards)

@keyboard_blueprint.route("/keyboards/<id>")
def show_by_brand(id):
    keyboards = keyboard_repository.select_by_brand(id)
    return render_template("keyboards/view-keyboards.html", keyboards=keyboards)

@keyboard_blueprint.route("/keyboards/new")
def new_keyboard():
    brands = brand_repository.select_all()
    return render_template("keyboards/new-keyboard.html", brands=brands)

@keyboard_blueprint.route("/keyboards", methods=["POST"])
def create_keyboard():
    name = request.form["name"]
    brand_id = request.form["brand"]
    description = request.form["description"]
    current_stock = request.form["current_stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    brand = brand_repository.select(brand_id)
    new_keyboard = Keyboard(name, brand, description, current_stock, cost_price, sale_price)
    keyboard_repository.save(new_keyboard)
    return redirect("/keyboards")

@keyboard_blueprint.route("/keyboards/<id>/edit")
def edit_keyboard(id):
    keyboard = keyboard_repository.select(id)
    brands = brand_repository.select_all()
    return render_template('keyboards/edit-keyboard.html', brands=brands, keyboard=keyboard)

@keyboard_blueprint.route("/keyboards/<id>", methods=["POST"])
def update_keyboard(id):
    name = request.form["name"]
    brand_id = request.form["brand_id"]
    description = request.form["description"]
    current_stock = request.form["current_stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    brand = brand_repository.select(brand_id)
    keyboard = Keyboard(name, brand, description, current_stock, cost_price, sale_price, id)
    keyboard_repository.update(keyboard)
    return redirect("/keyboards")