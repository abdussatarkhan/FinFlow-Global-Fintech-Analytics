import os
import pandas as pd

def test_data_generation():
    assert os.path.exists('data/dim_merchant.csv')
    assert os.path.exists('data/fact_transactions.csv')
    df = pd.read_csv('data/fact_transactions.csv')
    assert len(df) > 0
    assert 'net_revenue_usd' in df.columns
    assert df['net_revenue_usd'].sum() > 0
