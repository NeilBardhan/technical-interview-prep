## Run from CLI with python3 scripts/fake_products.py 200

import os
import sys
import pandas as pd
import random
from faker import Faker


def create_fake_product_df(num_products):
    fake = Faker()
    products = []
    categories = ["Electronics","Clothing","Books","Home","Toys"]
    for i in range(1, num_products+1):  # num_products products
        products.append([
            i,
            fake.word().capitalize(),
            random.choice(categories),
            round(random.uniform(5, 500), 2)
        ])
    products_df = pd.DataFrame(products, columns=["product_id","name","category","price"])
    return products_df


def write_data_to_file(df, file_path):
    file_name = "{}/products.csv".format(file_path)
    print("Writing product data to :", file_name)
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    number_of_products = sys.argv[1]
    print("Generating dataset for {} products.".format(number_of_products))
    products_df = create_fake_product_df(int(number_of_products))
    # print(products_df.head(2))
    save_path = "{}/datasets".format(os.getcwd())
    # print(save_path)
    write_data_to_file(products_df, save_path)