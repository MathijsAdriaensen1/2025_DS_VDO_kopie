from datetime import datetime
from app.db import execute_query


class Product:
    def __init__(self, name, price, description, active, image, brand_id=None, category_id=None, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.active = active
        self.image = image
        self.brand_id = brand_id
        self.category_id = category_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @classmethod
    def get_all(cls):
        query = """select * from products ORDER BY name"""
        results = execute_query(query, fetch=True)
        return results

    @classmethod
    def get_by_id(self, id):
        query = """select * from products where id = %s"""
        results = execute_query(query, id, fetchone=True)

    def save(self):
        query = """INSERT INTO products (name, price, description, active, image, created_at, updated_at)"""

    def update(self):
        pass

    def delete(self):
        pass

