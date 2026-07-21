from src.extract import extract_csv, extract_mcc_json

if __name__ == "__main__":
    users_df = extract_csv("users_data.csv")
    cards_df = extract_csv("cards_data.csv")
    merchant_category_df = extract_mcc_json("mcc_codes.json")
    transactions_df = extract_csv("transactions_data.csv")