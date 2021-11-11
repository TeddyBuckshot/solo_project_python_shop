import pdb 
from db.run_sql import run_sql
from models.brand import Brand
from models.keyboard import Keyboard

def save(brand):
    sql = "INSERT INTO brands (name, origin, active) VALUES (%s, %s, %s) RETURNING *"
    values = [
        brand.name, 
        brand.origin,
        brand.active
        ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    brand.id = id
    return brand

def update(brand):
    sql = "UPDATE brands SET (name, origin, active) = (%s, %s, %s) WHERE id = %s"
    values = [
        brand.name,
        brand.origin,
        brand.active,
        brand.id
        ]
    run_sql(sql, values)

def select(id):
    # pdb.set_trace()
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        brand = Brand(
            results['name'], 
            results['origin'],
            results['active'], 
            results['id']
            )
    return brand

def select_all():
    brands = []
    sql = "SELECT * FROM brands ORDER BY id"
    results = run_sql(sql)
    for row in results:
        brand = Brand(
            row['name'], 
            row['origin'], 
            row['active'],
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
    sql = "SELECT * FROM keyboards WHERE brand_id = %s"
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

def is_brand_active(brand):
    if brand.active == True:
        return True
    elif brand.active == False:
        return False

