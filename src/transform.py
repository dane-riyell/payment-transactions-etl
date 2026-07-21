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