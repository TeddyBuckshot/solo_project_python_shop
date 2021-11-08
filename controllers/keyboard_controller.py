from flask import Flask, render_template, Blueprint, request, redirect
from models.keyboard import Keyboard
import repositories.keyboard_repository as keyboard_repository


keyboard_blueprint = Blueprint("keyboards", __name__)


@keyboard_blueprint.route("/keyboards")
def keyboards():
    keyboards = keyboard_repository.select_all()
    return render_template("keyboards/view-keyboards.html", keyboards=keyboards)

@keyboard_blueprint.route("/keyboards/<id>")
def show_brands(id):
    keyboard = keyboard_repository.select(id)
    brands = keyboard_repository.get_brand(keyboard)
    return render_template("keyboards/view-manufacturer.html", brands=brands, keyboard=keyboard)