# Datasets for Technical Interviews

## Workflow

### 1. Activating the Poetry `.venv`

  1. `which poetry`
  2. `poetry install`
  3. `poetry env info --path`
  4. `source .venv/bin/activate` 

### 2. Creating an `ecommerce` database in `sqlite3`

  1. Create an empty `datasets/` directory in the project root.
  2. Run `source scripts/create_fake_datasets.sh` to create `customers.csv`, `products.csv`, `transactions.csv`, `transaction_items.csv` and `reviews.csv` in the `datasets/` directory.
  3. Run `sqlite3 datasets/ecommerce.db` to create an _empty_ `sqlite3` database.
  4. `python3 scripts/create_sqlite_tables.py datasets/ecommerce.db` to create empty tables in `ecommerce.db`. The SQL in the script enforces foreign key constraints.
  5. `python3 scripts/populate_sqlite_tables.py datasets/` to populate the tables created in the previous command with the `.csv`s generated in step 2.

This is all that is needed for Pandas and python.

#### Jupyter Lab for this `.venv`

  1. Create a kernel just for this `.venv` project `python -m ipykernel install --user --name=.venv --display-name="technical-interview-prep-pandas"`. This is only run once. The installed kernelspec `.venv` is in `/Users/neilbardhan/Library/Jupyter/kernels/.venv`