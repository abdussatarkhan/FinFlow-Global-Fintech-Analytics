-- Star Schema Data Warehouse DDL for FinFlow Global FinTech
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT, quarter INT, month INT, month_name VARCHAR(10),
    is_weekend BOOLEAN, is_quarter_end BOOLEAN
);

CREATE TABLE dim_merchant (
    merchant_id VARCHAR(32) PRIMARY KEY,
    merchant_name VARCHAR(100),
    industry VARCHAR(50),
    tier VARCHAR(20), -- Enterprise, Mid-Market, SMB
    country VARCHAR(3),
    onboarding_date DATE
);

CREATE TABLE dim_currency_corridor (
    corridor_id VARCHAR(10) PRIMARY KEY,
    source_currency VARCHAR(3),
    target_currency VARCHAR(3),
    base_fx_spread_bps NUMERIC(6, 2)
);

CREATE TABLE fact_transactions (
    transaction_id VARCHAR(64) PRIMARY KEY,
    date_id INT REFERENCES dim_date(date_id),
    merchant_id VARCHAR(32) REFERENCES dim_merchant(merchant_id),
    corridor_id VARCHAR(10) REFERENCES dim_currency_corridor(corridor_id),
    gross_amount_usd NUMERIC(12, 2),
    interchange_fee_usd NUMERIC(10, 4),
    fx_margin_usd NUMERIC(10, 4),
    net_revenue_usd NUMERIC(10, 4),
    is_fraud_flagged BOOLEAN
);
