## Run from CLI with python3 scripts/fake_reviews.py datasets/transactions_items.csv

import os
import sys
import random
import pandas as pd
from faker import Faker


def create_fake_reviews_df(transactions):
    fake = Faker()
    reviews = []
    num_reviews = random.randint(1, transactions.shape[0])
    for i in range(1, num_reviews+1):
        order_id = transactions["order_id"].sample(n=1).iloc[0] # Pick an order at random
        product_id = transactions.loc[transactions["order_id"]==order_id, 'product_id'].sample(n=1).iloc[0] # Pick a product at random
        rating = random.randint(1,5)
        review_date = fake.date_between(start_date="-3y", end_date="today")
        reviews.append([i, order_id, product_id, rating, review_date])

    reviews_df = pd.DataFrame(reviews, columns=["review_id","order_id","product_id","rating","review_date"])
    return reviews_df


def write_data_to_file(df, file_path):
    file_name = "{}/reviews.csv".format(file_path)
    print("Writing review data to :", file_name)
    df.to_csv(file_name, index=False)

if __name__ == '__main__':
    transactions_data_path = sys.argv[1]
    transactions = pd.read_csv(transactions_data_path)
    
    print("Generating reviews dataset.")
    reviews_df = create_fake_reviews_df(transactions)
    # print(reviews_df.head(2))

    save_path = "{}/datasets".format(os.getcwd())
    # print(save_path)
    write_data_to_file(reviews_df, save_path)


