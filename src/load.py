from src.db import engine
import time
from io import StringIO

def load_users(users_df):
    start = time.perf_counter()
    users_df.to_sql("users", engine, if_exists="append", index=False)
    elapsed = time.perf_counter() - start
    print(f"Loaded users table in {elapsed:.2f} seconds")

def load_merchant_category(merchant_category_df):
    start = time.perf_counter()
    merchant_category_df.to_sql("merchant_category", engine, if_exists="append", index=False)
    elapsed = time.perf_counter() - start
    print(f"Loaded merchant_category table in {elapsed:.2f} seconds")

def load_cards(cards_df):
    start = time.perf_counter()
    cards_df.to_sql("cards", engine, if_exists="append", index=False)
    elapsed = time.perf_counter() - start
    print(f"Loaded cards table in {elapsed:.2f} seconds")

def load_merchants(merchants_df):
    start = time.perf_counter()
    merchants_df.to_sql("merchants", engine, if_exists="append", index=False)
    elapsed = time.perf_counter() - start
    print(f"Loaded merchants table in {elapsed:.2f} seconds")

def load_transactions(transactions_df):
    start = time.perf_counter()

    # Create an in-memory CSV
    buffer = StringIO()
    transactions_df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    # Connect to PostgreSQL
    raw_conn = engine.raw_connection()
    cur = raw_conn.cursor()

    # SQL COPY command
    copy_sql = '''
        COPY transactions
        FROM STDIN
        WITH (FORMAT CSV)
    '''
    
    try:
        # Bulk load
        cur.copy_expert(copy_sql, buffer)
        # Save changes
        raw_conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
    
    elapsed = time.perf_counter() - start
    print(f"Loaded transactions table in {elapsed:.2f} seconds")