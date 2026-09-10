import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)
np.random.seed(42)

# Generate dim_merchant
merchants = []
for i in range(1, 201):
    merchants.append({
        'merchant_id': f'M_{i:04d}',
        'merchant_name': f'Merchant Enterprise {i}',
        'industry': np.random.choice(['SaaS', 'E-Commerce', 'Marketplace', 'Travel', 'Gaming']),
        'tier': np.random.choice(['Enterprise', 'Mid-Market', 'SMB'], p=[0.15, 0.35, 0.50]),
        'country': np.random.choice(['USA', 'GBR', 'DEU', 'SGP', 'ARE'])
    })
df_m = pd.DataFrame(merchants)
df_m.to_csv('data/dim_merchant.csv', index=False)

# Generate transactions
n_tx = 5000
tx_data = {
    'transaction_id': [f'TX_{i:07d}' for i in range(1, n_tx + 1)],
    'merchant_id': np.random.choice(df_m['merchant_id'], n_tx),
    'gross_amount_usd': np.round(np.random.exponential(scale=350, size=n_tx) + 10, 2),
    'is_fraud_flagged': np.random.choice([0, 1], size=n_tx, p=[0.985, 0.015])
}
df_tx = pd.DataFrame(tx_data)
df_tx['net_revenue_usd'] = np.round(df_tx['gross_amount_usd'] * np.random.uniform(0.018, 0.029, n_tx), 4)
df_tx.to_csv('data/fact_transactions.csv', index=False)
print("Synthetic FinTech transactions generated successfully in data/")
