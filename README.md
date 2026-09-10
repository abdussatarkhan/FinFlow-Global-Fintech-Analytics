# FinFlow — Global FinTech & Cross-Border Payment Analytics

[![CI](https://github.com/abdussatarkhan/FinFlow-Global-Fintech-Analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/abdussatarkhan/FinFlow-Global-Fintech-Analytics/actions)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16_Star_Schema-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-30+_DAX_Measures-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-Analytics_Engine-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Author](https://img.shields.io/badge/Author-Abdussatar-E50914?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abdussatarkhan)

> **Enterprise FinTech and Neo-Banking payment intelligence platform modeling multi-currency cross-border payment flows ($7.4B GPV), interchange margin yield, merchant cohort retention, and automated fraud anomaly detection.**

---

## 🏛️ System Architecture

```mermaid
graph TD
    subgraph Data Layer & Synthetic Engine
        Gen[Python FinTech Simulation Engine] --> CSVs[Star Schema Dimensional CSVs]
    end
    subgraph Data Warehouse
        CSVs --> DW[(PostgreSQL 16 Data Warehouse: 6 Dims, 4 Facts)]
        DW --> Views[Pre-Calculated Analytical BI Views]
    end
    subgraph Analytics & Intelligence
        Views --> PowerBI[Power BI Semantic Model + 30+ DAX Measures]
        Views --> Anomaly[Machine Learning 3DS Fraud Anomaly Classifier]
    end
```

---

## 📊 Visual Analytics & Performance Showcase

<div align="center">

| Executive KPI Hero | Cross-Border FX Corridors |
| :---: | :---: |
| ![Executive KPI](screenshots/01_executive_kpi_dashboard.png) | ![FX Corridors](screenshots/02_corridor_volume_heatmap.png) |

| Merchant Cohort Retention | ML Fraud Risk Scoring |
| :---: | :---: |
| ![Cohort Retention](screenshots/03_merchant_cohort_retention.png) | ![Fraud Anomaly](screenshots/04_fraud_risk_scatter.png) |

</div>

<div align="center">

[![Daily Streak](https://img.shields.io/badge/Daily%20Streak-Active%20%F0%9F%94%A5-brightgreen?style=flat-square&logo=github)](https://github.com/abdussatarkhan)
[![Master Portfolio](https://img.shields.io/badge/Portfolio-50%2B%20Enterprise%20Projects-0e75b6?style=flat-square&logo=github)](https://github.com/abdussatarkhan/abdussatarkhan)
[![Author: Abdussatar](https://img.shields.io/badge/Author-Abdussatar-24292e?style=flat-square&logo=github)](https://github.com/abdussatarkhan)

</div>


---

## 🌟 Key Technical Highlights

1. **Dimensional Star Schema**: Modeled for sub-second analytical slicing across currency pairs, payment rails (ACH, SEPA, Swift, FedNow), and merchant tiers.
2. **30+ Production DAX Measures**: Includes Net Take Rate, Blended Interchange Yield, Rolling 12-Month Merchant LTV, and Volume Churn Velocity.
3. **Automated Data Quality & CI/CD**: GitHub Actions pipeline automatically validates schema integrity and KPI computations.

---

## 🚀 Quickstart & Reproduction

```bash
# 1. Clone the repository
git clone https://github.com/abdussatarkhan/FinFlow-Global-Fintech-Analytics.git
cd FinFlow-Global-Fintech-Analytics

# 2. Install dependencies & run generator
pip install pandas numpy pytest
python scripts/01_generate_synthetic_data.py

# 3. Run test suite
pytest tests/ -v
```

---

## 🗺️ Roadmap & Upcoming Features

- [x] Multi-currency Star Schema data warehouse DDL
- [x] 24-Month merchant cohort retention model
- [x] Machine learning fraud anomaly probability scoring
- [ ] Real-time Kafka streaming payment ingestion worker
- [ ] Automated dbt-core data test suite

---

## 👨‍💻 Author & Profile

Built by **Abdussatar** ([@abdussatarkhan](https://github.com/abdussatarkhan)).  
Connect on [LinkedIn](https://www.linkedin.com/in/abdus-satar-5150813b5/) or explore other repositories on [GitHub](https://github.com/abdussatarkhan).

---

## 📜 License
MIT License — see LICENSE for details.


---

<div align="center">

### 👨‍💻 Maintained by [Abdussatar (@abdussatarkhan)](https://github.com/abdussatarkhan)
Part of the **[Master Enterprise Data Analytics & AI Portfolio](https://github.com/abdussatarkhan/abdussatarkhan)**.

⭐ If you find this repository valuable, consider dropping a star! ⭐

</div>
