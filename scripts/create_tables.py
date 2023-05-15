import os
from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric
from sqlalchemy.orm import declarative_base
from sqlalchemy import inspect


Base = declarative_base()

class Customers(Base):
    """
    Customer table with customer information.
    """
    __tablename__ = 'customers'
    cust_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    since = Column(Date, nullable=False)
    group = Column(String(255))

class Representatives(Base):
    """
    Representative table with representative information.
    """
    __tablename__ = 'representatives'
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
    cust_id = Column(Integer)
    street = Column(String(255))
    post_code = Column(String(255))

class Products(Base):
    """
    Product table with product information.
    """
    __tablename__ = 'products'
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
    shop_id = Column(Integer)
    since = Column(Date, nullable=False)

class Purchase(Base):
    """
    Purchase table with purchase information.
    """
    __tablename__ = 'purchase'
    purch_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer)
    date = Column(Date)
    product_id = Column(Integer)
    amount = Column(Integer)
    total_price = Column(Numeric)
    shop_id = Column(Integer)
    employee_id = Column(Integer)


def create_tables():
    """
    Creates tables in DB
    """
    db_url = (
        "postgresql://"
        f"{os.environ['POSTGRES_USER']}:"
        f"{os.environ['POSTGRES_PASSWORD']}@"
        f"{os.environ['POSTGRES_HOST']}:"
        f"{os.environ['POSTGRES_PORT']}/"
        f"{os.environ['POSTGRES_DB']}"
    )

    engine = create_engine(db_url, echo = True)

    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    required_tables = [
        "customers",
        "representatives",
        "address",
        "products",
        "shops",
        "employees",
        "purchase",
    ]

    # Check if all required tables exist
    if all(table in table_names for table in required_tables):
        print("All tables already exist. Skipping table creation.")
    else:
    # Create predefined tables
        print("Creating tables...")
        Base.metadata.create_all(engine)
        print("Tables created successfully.")

if __name__ == '__main__':
    create_tables()
