from flask import Flask, render_template, Blueprint, request, redirect
import repositories.category_repository as category_repository

category_blueprint = Blueprint("categories", __name__)

@category_blueprint.route("/categories")
def show_categories():
    categories = category_repository.select_all()
    return render_template("brands/view-brands.html", categories = categories)