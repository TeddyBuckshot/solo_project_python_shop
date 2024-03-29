
from db.run_sql import run_sql
from models.brand import Brand
from models.keyboard import Keyboard
from models.category import Category
import repositories.brand_repository as brand_repository
import repositories.category_repository as category_repository

def save(keyboard):
    sql = "INSERT INTO keyboards (name, brand_id, description, category_id, current_stock, cost_price, sale_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [
        keyboard.name,
        keyboard.brand.id,
        keyboard.description,
        keyboard.category.id,
        keyboard.current_stock,
        keyboard.cost_price,
        keyboard.sale_price
        ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    keyboard.id = id
    return keyboard

def update(keyboard):
    sql = "UPDATE keyboards SET (name, brand_id, description, current_stock, cost_price, sale_price) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        keyboard.name,
        keyboard.brand.id,
        keyboard.description,
        keyboard.current_stock,
        keyboard.cost_price,
        keyboard.sale_price,
        keyboard.id
        ]
    run_sql(sql, values)

def select(id):
    keyboard = None
    sql = "SELECT * FROM keyboards WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        brand = brand_repository.select(results['brand_id'])
        category = category_repository.select(results['category_id'])
        keyboard = Keyboard(
            results['name'], 
            brand, 
            results['description'], 
            category,
            results['current_stock'], 
            results['cost_price'], 
            results['sale_price'], 
            results['id']
            )
    return keyboard

def select_all():
    keyboards = []
    sql = "SELECT * FROM keyboards ORDER BY brand_id"
    results = run_sql(sql)
    for row in results:
        brand = brand_repository.select(row['brand_id'])
        category = category_repository.select(row['category_id'])
        keyboard = Keyboard(
            row['name'], 
            brand, 
            row['description'],
            category,
            row['current_stock'], 
            row['cost_price'], 
            row['sale_price'], 
            row['id']
            )
        keyboards.append(keyboard)
    return keyboards

def select_by_brand(id):
    keyboards = []
    sql = "SELECT * FROM keyboards WHERE brand_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for row in results:
        brand = brand_repository.select(row['brand_id'])
        category = category_repository.select(row['category_id'])
        keyboard = Keyboard(
            row['name'], 
            brand, 
            row['description'], 
            category,
            row['current_stock'], 
            row['cost_price'], 
            row['sale_price'], 
            row['id']
            )
        keyboards.append(keyboard)
    return keyboards

def delete(id):
    sql = "DELETE FROM keyboards WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM keyboards"
    run_sql(sql)


# def get_brand(keyboard):
#     brands = []
#     sql = "SELECT * FROM brands WHERE id = %s"
#     values = [keyboard.brand.id]
#     results = run_sql(sql, values)
#     for row in results:
#         brand = Brand(
#             row['name'], 
#             row['origin'], 
#             row['id']
#             )
#         brands.append(brand)
#     return brands