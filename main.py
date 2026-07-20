from src.extract import extract_csv, extract_mcc_json

if __name__ == "__main__":
    cards = extract_csv("cards_data.csv")
    transactions = extract_csv("transactions_data.csv")
    users = extract_csv("users_data.csv")
    merchant_category = extract_mcc_json("mcc_codes.json")