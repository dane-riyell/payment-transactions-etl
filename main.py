from src.logging_config import setup_logging

setup_logging()

from src.extract import extract_csv, extract_mcc_json
from src.transform import (
    transform_users,
    transform_cards,
    transform_merchant_category,
    transform_merchants,
    transform_transactions
)
from src.load import (
    truncate_all_tables,
    load_users,
    load_merchant_category,
    load_cards,
    load_merchants,
    load_transactions
)

if __name__ == "__main__":
    users_df = extract_csv("users_data.csv")
    cards_df = extract_csv("cards_data.csv")
    merchant_category_df = extract_mcc_json("mcc_codes.json")
    transactions_df = extract_csv("transactions_data.csv")

    users_df = transform_users(users_df)
    cards_df = transform_cards(cards_df)
    merchant_category_df = transform_merchant_category(merchant_category_df)
    merchants_df = transform_merchants(transactions_df)
    transactions_df = transform_transactions(transactions_df)

    truncate_all_tables()

    load_users(users_df)
    load_merchant_category(merchant_category_df)
    load_cards(cards_df)
    load_merchants(merchants_df)
    load_transactions(transactions_df)