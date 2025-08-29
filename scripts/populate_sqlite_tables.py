import os
import sys
import sqlite3
import argparse
import pandas as pd


def print_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
    cursor.close()


def populate_table_with_csv(connection, table_name, csv_file_path):
    df = pd.read_csv(csv_file_path)
    print('Inserting data from {} to {}'.format(csv_file_path.split('/')[-1], table_name))
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    cursor = connection.cursor()
    count_sql = "SELECT count(*) FROM {}".format(table_name)
    cursor.execute(count_sql)
    num_rows = cursor.fetchall()[0][0]
    print("{} rows inserted.".format(num_rows))
    cursor.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('datasets_root')
    args = parser.parse_args()
    # print(args.__dict__)

    datasets_root = "{}/{}".format(os.getcwd(), args.datasets_root)
    db_file_path = "{}{}".format(datasets_root, 'ecommerce.db')
    customer_csv_file_path = "{}{}".format(datasets_root, 'customers.csv')
    product_csv_file_path = "{}{}".format(datasets_root, 'products.csv')
    transactions_csv_file_path = "{}{}".format(datasets_root, 'transactions.csv')
    transactions_items_csv_file_path =  "{}{}".format(datasets_root, 'transactions_items.csv')
    reviews_csv_file_path =  "{}{}".format(datasets_root, 'reviews.csv')

    if os.path.isfile(db_file_path):
        with sqlite3.connect(db_file_path) as connection:
            populate_table_with_csv(connection, 'customer', customer_csv_file_path)
            populate_table_with_csv(connection, 'product', product_csv_file_path)
            populate_table_with_csv(connection, 'transactions', transactions_csv_file_path)
            populate_table_with_csv(connection, 'transaction_items', transactions_items_csv_file_path)
            populate_table_with_csv(connection, 'reviews', reviews_csv_file_path)
            print_tables(connection)
        connection.close()
        