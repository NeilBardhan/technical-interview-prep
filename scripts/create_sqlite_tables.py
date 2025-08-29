import os
import sys
import sqlite3

def print_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
    cursor.close()


def create_customer_table(connection):
    create_customer_table_sql = """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        signup_date DATE,
        country TEXT
    );
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS customer")
    cursor.execute(create_customer_table_sql)
    cursor.close()


def create_product_table(connection):
    create_product_table_sql = """
    CREATE TABLE IF NOT EXISTS product (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        price FLOAT
    );
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS product")
    cursor.execute(create_product_table_sql)
    cursor.close()


def create_transaction_tables(connection):
    create_transaction_table_sql = """
    CREATE TABLE IF NOT EXISTS transactions (
        order_id INTEGER PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        total_amount FLOAT,
        FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
    );
    """

    create_transaction_items_table_sql = """
    CREATE TABLE IF NOT EXISTS transaction_items (
        order_item_id INTEGER PRIMARY KEY,
        order_id INT,
        product_id INT,
        quantity INT,
        item_price FLOAT,
        FOREIGN KEY (order_id) REFERENCES transactions (order_id),
        FOREIGN KEY (product_id) REFERENCES product (product_id)
    );
    """

    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute(create_transaction_table_sql)
    
    cursor.execute("DROP TABLE IF EXISTS transaction_items")
    cursor.execute(create_transaction_items_table_sql)
    cursor.close()


def create_review_table(connection):
    create_review_table_sql = """
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY,
        order_id INT,
        product_id INT,
        rating INT,
        review_date DATE,
        FOREIGN KEY (order_id) REFERENCES transactions (order_id),
        FOREIGN KEY (product_id) REFERENCES product (product_id)
    );
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS reviews")
    cursor.execute(create_review_table_sql)
    cursor.close()

if __name__ == '__main__':
    path_to_sqlite_db = "{}/{}".format(os.getcwd(), sys.argv[1])
    print(path_to_sqlite_db)

    with sqlite3.connect(path_to_sqlite_db) as connection:
        create_customer_table(connection)
        connection.commit()

        create_product_table(connection)
        connection.commit()

        create_transaction_tables(connection)
        connection.commit()

        create_review_table(connection)
        connection.commit()

        print_tables(connection)
        
    connection.close()