from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

# User Database Model
class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String)
    email = Column(String)
    address = Column(String)


class Category(Base):
    
    __tablename__ = "categorys"
    
    id = Column(Integer, primary_key=True, index=True)
    product_category = Column(String, unique=True)


class Product(Base):
    
    __tablename__ = "procucts"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, unique=True)
    product_price = Column(Integer)
    product_description = Column(String)
    product_category = Column(Integer, ForeignKey('categorys.id'))
    users_id = Column(Integer, ForeignKey('users.id'))

    users = relationship("User")


class UserCart(Base):

    __tablename__ = "usercarts"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    product_name = Column(String, unique=True)
    product_price = Column(Integer)

    users_id = Column(Integer, ForeignKey('users.id'))
    products_id = Column(Integer, ForeignKey('users.id'))


class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    products_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Boolean, default=False)


class UserProduct(Base):

    __tablename__ = "userproducts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    status = Column(Boolean, default=True)
