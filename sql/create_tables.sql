DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS merchant_category;

CREATE TABLE users(
    user_id INT PRIMARY KEY,
    current_age INT NOT NULL,
    retirement_age INT NOT NULL,
    birth_year INT NOT NULL,
    birth_month INT NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender in ('M', 'F', 'O')),
    per_capita_income DECIMAL NOT NULL,
    yearly_income DECIMAL NOT NULL,
    total_debt DECIMAL NOT NULL,
    credit_score INT NOT NULL,
    num_credit_cards INT NOT NULL
);

CREATE TABLE merchant_category(
    mcc INT PRIMARY KEY, 
    classification TEXT NOT NULL
);

CREATE TABLE cards(
    card_id INT PRIMARY KEY, 
    user_id INT NOT NULL REFERENCES users(user_id),
    card_brand TEXT NOT NULL,
    card_type TEXT NOT NULL,
    expiration_date DATE NOT NULL,
    has_chip BOOLEAN NOT NULL,
    credit_limit DECIMAL NOT NULL,
    acct_open_date DATE NOT NULL,
    year_pin_last_changed INT NOT NULL
);

CREATE TABLE merchants(
    merchant_id INT PRIMARY KEY,
    mcc INT REFERENCES merchant_category(mcc),
    merchant_city TEXT NOT NULL, 
    merchant_state TEXT,
    zip TEXT
);

CREATE TABLE transactions(
    transaction_id INT PRIMARY KEY, 
    user_id INT NOT NULL REFERENCES users(user_id),
    card_id INT NOT NULL REFERENCES cards(card_id),
    merchant_id INT NOT NULL REFERENCES merchants(merchant_id),
    amount DECIMAL NOT NULL,
    date DATE NOT NULL, 
    transaction_type TEXT NOT NULL,
    errors TEXT
);