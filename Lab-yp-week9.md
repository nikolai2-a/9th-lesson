
***1 zadanie***

```Python
import sqlite3
conn = sqlite3.connect(”users.db”)
cursor.execute(”CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT”)
cursor.execute(”CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL”)
cursor.executemany(”INSERT INTO customers(name) VALUES (?)[(”Ivan”), (”Peter”), (”Kolya”), (”Serj”)]”)
cursor.executemany(”INSERT INTO orders(customer_id, amount) VALUES (?, ?)[(3, 100500), (1, 100.5), (4, 123), (2, 246), (1, 369.5)]”)

#Пересоздаем таблтцу
cursor.execute(”CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL FOREIGN KEY(customer_id) REFERENCES customers(id)”)

cursor.execute(”INSERT INTO orders(customer_id, amount) VALIUES (999, 66.6)”)

#Sql запрос для того, чтобы FOREIGN KEY заработал
cursorexecute(”PRAGMA foreign_keys = ON;”)

#Как написать создание таблтцы, чтобы можно было удалить элементы таблицы customers
cursor.execute(”CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id) REFERENCES customers(id) ON DELETE CASCADE”)
#Если создаем таблицу (по умалчанию RESTRICT) и хотим что-то другое при удалении, то пишем ON DELETE, тогда порядок 1)RESTRICT 2)CASCADE 3)SET NULL 4)SET DEFAULT 5)NO ACTION - что происходит при удалении
```

```Python
#ORM -Object Relational Mapping
#Примеры: SQLALchemy, DjangoORM, PeeWee, SQLModel, TortoiseORM

cursor.execute(f”SELECT * FROM students WHERE name = ‘{user_input}’”)
# а) Petya
# б) Petya’and drop table students
#
#>>pip install sqlalchemy
#
#Engine - 
#Core - построение sql команд из питоновсих выражений
#ORM - 
```

```Python
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Floats, Boolean

engine = create_engine(‘sqlite:///database.db;’)
engine.connect()
metadata = MetaData()
studrnts_table = Table(
		‘students’, 
		‘metadata’, 
		Column(’id’, Integer, primary_key = True),
		Column(’name’, String(100), nullable = False), 
		Column(’group’, String(20)), 
		Column(’gpa’, Float, default = 0.0), 
		Column(’is_active’, Boolean, default = True),
		)

metadata create_all(engine)
with engine.connect() as connector:
	something = insert(students_table).values(
			name = ‘Иванов И И’,
			group = ‘ИУ10-33’,
			gpa = 4.5,
			)
	result = connection.execute(something)
	connection.commit()
	print(f”Добавлена строка с id={result.inserted_primary_key[0]}”)

# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db

#smt = insert(students_table)
#data = [
#{’name’=‘Petrov P P’, ‘group’=‘IU10-31’, ‘gpa’=3.8}, 
#{’name’=‘Sidorov S S’, ‘group’=‘IU10-35’, ‘gpa’=4.0},
#]
#Result = connection.execute(smt, data)
```

