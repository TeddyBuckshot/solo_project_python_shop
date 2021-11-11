from db.run_sql import run_sql
from models.brand import Brand
from models.keyboard import Keyboard
from models.category import Category

def save(category):
    sql = "INSERT INTO categories (name) VALUES (%s) RETURNING *"
    values = [category.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    category.id = id
    return category

def select_all():
    categories = []
    sql = "SELECT * FROM categories ORDER BY id"
    results = run_sql(sql)
    for row in results:
        category = Category(
            row['name'], 
            row['id']
            )
        categories.append(category)
    return categories

def select(id):
    # pdb.set_trace()
    category = None
    sql = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        category = Category(
            results['name'],
            results['id']
            )
    return category