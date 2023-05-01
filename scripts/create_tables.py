import os
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Customer(Base):
    """
    Customer table with customer information.
    """
    __tablename__ = 'customer'
    cust_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    since = Column(Date, nullable=False)
    group = Column(String(255))

class Representative(Base):
    """
    Representative table with representative information.
    """
    __tablename__ = 'representative'
    representative_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    position = Column(String(255))

class Address(Base):
    """
    Address table with customer address information.
    """
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    street = Column(String(255))
    post_code = Column(String(255))

class Product(Base):
    """
    Product table with product information.
    """
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(255))
    unit_price = Column(Numeric)

class Shops(Base):
    """
    Shops table with shop information.
    """
    __tablename__ = 'shops'
    shop_id = Column(Integer, primary_key=True)
    street = Column(String(255))
    city = Column(String(255))
    size = Column(Integer)

class Employees(Base):
    """
    Employees table with employee information.
    """
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.shop_id'))
    since = Column(Date, nullable=False)

class Purchase(Base):
    """
    Purchase table with purchase information.
    """
    __tablename__ = 'purchase'
    purch_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey('customer.cust_id'))
    date = Column(Date)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    amount = Column(Integer)
    total_price = Column(Numeric)
    shop_id = Column(Integer, ForeignKey('shops.shop_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))


def create_tables():
    """
    Creates tables in DB
    """
    db_url = (
        "postgresql://"
        f"{os.environ['POSTGRES_USER']}:"
        f"{os.environ['POSTGRES_PASSWORD']}@"
        f"{os.environ['POSTGRES_HOST']}:"
        "5432/"
        f"{os.environ['POSTGRES_DB']}"
    )

    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()
    