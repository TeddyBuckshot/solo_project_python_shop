from db.run_sql import run_sql
from models.brand import Brand
from models.keyboard import Keyboard

def save(brand):
    sql = "INSERT INTO brands (name, origin) VALUES (%s, %s) RETURNING *"
    values = [brand.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    brand.id = id
    return brand

def update(brand):
    sql = "UPDATE brands SET (name, origin) = (%s, %s) WHERE id = %s"
    values = [
        brand.name,
        brand.origin,
        brand.id
        ]
    run_sql(sql, values)

def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        brand = Brand(
            results['name'], 
            results['origin'], 
            results['id']
            )
    return brand

def select_all():
    brands = []
    sql = "SELECT * FROM brands"
    results = run_sql(sql)
    for row in results:
        brand = Brand(
            row['name'], 
            row['origin'], 
            row['id']
            )
        brands.append(brand)
    return brands

def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)

def get_all_keyboards(brand):
    keyboards = []
    sql = "SELECT * FROM keyboards WHERE user_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)
    for row in results:
        keyboard = Keyboard(
            row['name'],
            brand,
            row['description'],
            row['current_stock'],
            row['cost_price'],
            row['sale_price'],
            row['id']
            )
        keyboards.append(keyboard)
    return keyboards
