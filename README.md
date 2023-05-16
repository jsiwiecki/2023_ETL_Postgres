# 2023_ETL_Postgres

### Brief description
This project is about to ingest json data into a PostgresSQL database and then using PySpark for data processing.


### Technology:
- PostgreSQL,
- Docker,
- SQLAlchemy,
- Python,
- PySpark.


### Data Model
1. Customer
* CUST_ID (Primary Key)
* NAME
* SINCE
* GROUP

2.Representative
* REPRESENTATIVE_ID
* NAME
* SURNAME
* POSITION

2. Address
* ADRESS_ID (PK)
* CUST_ID (Foreign Key referencing Customer tbl)
* STREET
* POST_CODE

3. Purchase
* PURCH_ID (PK)
* CUST_ID (FK referencing Customer)
* DATE
* PRODUCT_ID (FK referencing Product)
* AMOUNT
* TOTAL_PRICE
* SHOP_ID (FK referencing Shops)
* EMPLOYEE_ID (FK referencing Employees)

4. Product
* PRODUCT_ID (PK)
* NAME
* CATEGORY
* UNIT_PRICE

5. Shops
* SHOP_ID (PK)
* STREET
* CITY
* SIZE

6. Employees
* EMPLOYEE_ID (PK)
* NAME
* SURNAME
* SHOP_ID (FK referencing Shops)
* SINCE

# How to run
Enter 