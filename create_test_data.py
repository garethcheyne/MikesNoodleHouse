from sqlalchemy import create_engine, insert, select, update, delete, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from database.models import Base, User, Product
from helpers import *

# Init DB
engine = create_engine(f"sqlite:///database/database.db", echo=True) # echo=True for debug
Session = sessionmaker(bind=engine)
session = Session()

# Create tables from models
Base.metadata.create_all(engine)


# Create Test date for products
products = [
    {'id': 0, 'name': 'Noodles', 'description': 'Noodles', 'costIncl': 10.00},
    {'id': 1, 'name': 'Meat Pie', 'description': 'Noodles', 'costIncl': 8.5},
    {'id': 2, 'name': 'Chicken Pie', 'description': 'Noodles', 'costIncl': 1.5},
    {'id': 3, 'name': 'Cheese Roll', 'description': 'Noodles', 'costIncl': 3.5},
    {'id': 4, 'name': 'Nuts', 'description': 'Noodles', 'costIncl': 6.5},
    {'id': 5, 'name': 'Soap', 'description': 'Noodles', 'costIncl': 8.5},
    {'id': 6, 'name': 'Pancakes', 'description': 'Noodles', 'costIncl': 10.00},
    {'id': 7, 'name': 'Bis', 'description': 'Noodles', 'costIncl': 7.5},
    {'id': 8, 'name': 'Pizza', 'description': 'Noodles', 'costIncl': 8.5},
    {'id': 9, 'name': 'Coke', 'description': 'Noodles', 'costIncl': 4.5}
    ]

for p in products:
    product = Product(name=p['name'], description=p['description'], costIncl=p['costIncl']) 
    session.add(product)
    session.commit()


# Create Admin user
admin = User(id=0, username="admin", fullname="Admin", password= hash_password("admin"), level=0) 
session.add(admin)
session.commit()
