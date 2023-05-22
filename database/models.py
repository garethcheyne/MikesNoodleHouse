from sqlalchemy import Column, Integer, String, Numeric

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    fullname = Column(String(255))
    password = Column(String(255))
    level = Column(Integer)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    costIncl = Column(Numeric)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)

class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
