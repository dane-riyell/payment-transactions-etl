def transform_users(users_df):
    to_numeric_cols = ["yearly_income", "total_debt", "per_capita_income"]
    users_df[to_numeric_cols] = users_df[to_numeric_cols].replace(r"\$", "", regex=True)
    users_df = users_df.astype({
            "yearly_income":float,
            "total_debt":float,
            "per_capita_income":float
        })
    
    users_df = users_df.rename(columns={"id":"user_id"})

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

    return cards_df

def transform_merchant_category(merchant_category_df):
    merchant_category_df = merchant_category_df.astype({"mcc":int})
    return merchant_category_df