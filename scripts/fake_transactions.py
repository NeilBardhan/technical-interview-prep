## Run from CLI with python3 scripts/fake_transactions.py datasets/customers.csv datasets/products.csv

import os
import sys
import random
import pandas as pd
from faker import Faker


def create_fake_transactions_df(customers_df, products_df):
    fake = Faker()
    orders = []
    order_items = []
    order_id = 1
    order_item_id = 1

    for customer_id in customers_df["customer_id"]:
        for _ in range(random.randint(1,10)):  # each customer 1–10 orders
            order_date = fake.date_between(start_date="-3y", end_date="today")
            order_total = 0
            items = []
            for _ in range(random.randint(1,5)):  # 1–5 items per order
                product_id = products_df["product_id"].sample(n=1).iloc[0] # Pick a product at random
                quantity = random.randint(1,3)
                item_price = products_df.loc[products_df["product_id"]==product_id,"price"].values[0]
                order_total += quantity*item_price
                items.append([order_item_id, order_id, product_id, quantity, item_price])
                order_item_id += 1
            orders.append([order_id, customer_id, order_date, round(order_total,2)])
            order_items.extend(items)
            order_id += 1

    transactions_df = pd.DataFrame(orders, columns=["order_id","customer_id","order_date","total_amount"])
    transaction_items_df = pd.DataFrame(order_items, columns=["order_item_id","order_id","product_id","quantity","item_price"])
    return transactions_df, transaction_items_df


def write_data_to_file(df, file_name, note=""):
    
    print("Writing {} data to :{}".format(note, file_name))
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    customer_data_path = sys.argv[1]
    product_data_path = sys.argv[2]

    customers = pd.read_csv(customer_data_path)
    products = pd.read_csv(product_data_path)

    print("Generating transactions dataset for {} customers and {} products.".format(customers.shape[0], products.shape[0]))
    transactions_df, transaction_items_df = create_fake_transactions_df(customers, products)
    # print(transactions_df.head(2))
    # print(transaction_items_df.head(2))

    save_path = "{}/datasets".format(os.getcwd())
    # print(save_path)
    transactions_file_name = "{}/transactions.csv".format(save_path)
    transactions_items_file_name = "{}/transactions_items.csv".format(save_path)
    write_data_to_file(transactions_df, transactions_file_name)
    write_data_to_file(transaction_items_df, transactions_items_file_name)
    