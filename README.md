# Datasets for Technical Interviews

## Workflow

### 1. Activating the Poetry `.venv`

  1. `which poetry`
  2. `poetry install`
  3. `poetry env info --path`
  4. `source .venv/bin/activate` 

### 2. Generating Fake ecommerce `.csv` files

Run `source scripts/create_fake_datasets.sh` to create `customers.csv`, `products.csv`, `transactions.csv`, `transaction_items.csv` and `reviews.csv`

This is all that is needed for Pandas and python.

#### Jupyter Lab for this `.venv`

  1. Create a kernel just for this `.venv` project `python -m ipykernel install --user --name=.venv --display-name="technical-interview-prep-pandas"`. This is only run once. The installed kernelspec `.venv` is in `/Users/neilbardhan/Library/Jupyter/kernels/.venv`