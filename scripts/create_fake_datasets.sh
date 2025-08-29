#!/bin/bash

echo $(pwd)
python3 scripts/fake_customers.py 750
python3 scripts/fake_products.py 200
python3 scripts/fake_transactions.py datasets/customers.csv datasets/products.csv
python3 scripts/fake_reviews.py datasets/transactions_items.csv
