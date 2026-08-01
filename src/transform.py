import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_users(users_df):
    to_numeric_cols = ["yearly_income", "total_debt", "per_capita_income"]
    users_df[to_numeric_cols] = users_df[to_numeric_cols].replace(r"\$", "", regex=True)
    users_df = users_df.astype({
            "yearly_income":float,
            "total_debt":float,
            "per_capita_income":float
        })
    
    users_df = users_df.rename(columns={"id":"user_id"})

    users_df["gender"] = users_df["gender"].str.upper().map({"FEMALE":"F", "MALE":"M"})

    users_df = users_df[[
        "user_id",
        "current_age",
        "retirement_age",
        "birth_year",
        "birth_month",
        "gender",
        "per_capita_income",
        "yearly_income",
        "total_debt",
        "credit_score",
        "num_credit_cards"
    ]]

    logger.info(f"users_df transformed: {users_df.shape}")
    return users_df

def transform_cards(cards_df):
    cards_df["has_chip"] = cards_df["has_chip"].str.upper().map({"YES":True, "NO":False})
    cards_df["credit_limit"] = cards_df["credit_limit"].replace(r"\$", "", regex=True)

    cards_df["expires"] = pd.to_datetime(cards_df["expires"], format="%m/%Y")
    cards_df["acct_open_date"] = pd.to_datetime(cards_df["acct_open_date"], format="%m/%Y")    
    cards_df = cards_df.astype({
        "credit_limit":float
    })

    cards_df = cards_df.rename(columns={"id":"card_id", "client_id":"user_id", "expires":"expiration_date"})

    cards_df = cards_df[[
        "card_id",
        "user_id",
        "card_brand",
        "card_type",
        "expiration_date",
        "has_chip",
        "credit_limit",
        "acct_open_date",
        "year_pin_last_changed"
    ]]

    logger.info(f"cards_df transformed: {cards_df.shape}")
    return cards_df

def transform_merchant_category(merchant_category_df):
    merchant_category_df = merchant_category_df.astype({"mcc":int})

    logger.info(f"merchant_category_df transformed: {merchant_category_df.shape}")
    return merchant_category_df

def transform_merchants(transactions_df): #US only has 50 states but some merchant ids have 99 unique states 
    physical_transactions_df = transactions_df[transactions_df['merchant_city'].str.upper() != 'ONLINE']
    physical_transactions_df = physical_transactions_df.groupby('merchant_id').agg(
        mcc = ('mcc', lambda x: x.mode()[0]),
        merchant_city = ('merchant_city', lambda x: x.mode()[0]),
        merchant_state = ('merchant_state', lambda x: x.mode()[0] if not x.mode().empty else None),
        zip = ('zip', lambda x: x.mode()[0] if not x.mode().empty else None)
    ).reset_index()

    online_transactions_df = transactions_df[transactions_df['merchant_city'].str.upper() == 'ONLINE']
    online_transactions_df = online_transactions_df.groupby('merchant_id').agg(
        mcc = ('mcc', lambda x: x.mode()[0])
    ).reset_index()

    online_transactions_df['merchant_city'] = 'ONLINE'
    online_transactions_df['merchant_state'] = None
    online_transactions_df['zip'] = None

    merchants_df = pd.concat([physical_transactions_df, online_transactions_df], axis=0, ignore_index=True)
    merchants_df = merchants_df.drop_duplicates(subset='merchant_id', keep='first', ignore_index=True)
    merchants_df['zip'] = merchants_df['zip'].astype('Int64').astype('string')

    logger.info(f"merchants_df transformed: {merchants_df.shape}")
    return merchants_df

def transform_transactions(transactions_df):
    transactions_df = transactions_df.rename(
        columns=({
            'id':'transaction_id',
            'client_id':'user_id',
            'use_chip':'transaction_type'

        })
    )

    transactions_df['amount'] = transactions_df['amount'].replace(r"\$", "", regex=True).astype(float)
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    transactions_df = transactions_df[[
        'transaction_id',
        'user_id',
        'card_id',
        'merchant_id',
        'amount',
        'date',
        'transaction_type',
        'errors'
    ]]

    logger.info(f"transactions_df transformed: {transactions_df.shape}")
    return transactions_df