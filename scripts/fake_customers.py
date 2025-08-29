## Run from CLI with python3 scripts/fake_customers.py 750

import os
import sys
import pandas as pd
import random
from faker import Faker


def create_fake_customer_df(num_customers):
    fake = Faker()
    customers = []
    for i in range(1, num_customers+1):  # num_customers customers
        customers.append([
            i,
            fake.name(),
            fake.unique.email(),
            fake.date_between(start_date="-3y", end_date="today"),
            fake.country()
        ])
    customers_df = pd.DataFrame(customers, columns=["customer_id","name","email","signup_date","country"])
    return customers_df


def write_data_to_file(df, file_path):
    file_name = "{}/customers.csv".format(file_path)
    print("Writing customer data to :", file_name)
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    number_of_customers = sys.argv[1]
    print("Generating dataset for {} customers.".format(number_of_customers))
    customer_df = create_fake_customer_df(int(number_of_customers))
    # print(customer_df.head(2))
    save_path = "{}/datasets".format(os.getcwd())
    # print(save_path)
    write_data_to_file(customer_df, save_path)