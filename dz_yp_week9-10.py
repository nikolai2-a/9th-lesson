import json
import sqlite3


with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

print(f"Загружено товаров: {len(catalog)}")

categories = {}
products = []

for item in catalog:
    cat = item["category"]
    cat_name = cat["name"]
    cat_desc = cat["description"]

    categories.setdefault(cat_name, cat_desc)

    products.append({
        "product_name": item["product_name"],
        "price": item["price"],
        "category_name": cat_name
    })

print(f"Уникальных категорий: {len(categories)}")
print(f"Товаров: {len(products)}")

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS categories")

cursor.execute("""
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
""")

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL CHECK (price >= 0),
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
    )
""")

for cat_name, cat_desc in categories.items():
    cursor.execute(
        "INSERT INTO categories(name, description) VALUES (?, ?)",
        (cat_name, cat_desc)
    )

cursor.execute("SELECT id, name FROM categories")
category_ids = {name: cat_id for cat_id, name in cursor.fetchall()}

products_data = [
    (p["product_name"], p["price"], category_ids[p["category_name"]])
    for p in products
]

cursor.executemany(
    "INSERT INTO products(product_name, price, category_id) VALUES (?, ?, ?)",
    products_data
)

conn.commit()
