# Data Dictionary

## dim_fund

| Column Name       | Data Type | Description                                |
| ----------------- | --------- | ------------------------------------------ |
| amfi_code         | INTEGER   | Unique AMFI scheme identifier              |
| fund_house        | TEXT      | Mutual fund company name                   |
| scheme_name       | TEXT      | Name of mutual fund scheme                 |
| category          | TEXT      | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category      | TEXT      | Detailed category classification           |
| plan              | TEXT      | Direct or Regular plan                     |
| benchmark         | TEXT      | Benchmark index                            |
| expense_ratio_pct | REAL      | Expense ratio percentage                   |
| risk_category     | TEXT      | Risk classification                        |

---

## fact_nav

| Column Name | Data Type | Description      |
| ----------- | --------- | ---------------- |
| amfi_code   | INTEGER   | AMFI scheme code |
| date        | DATE      | NAV date         |
| nav         | REAL      | Net Asset Value  |

---

## fact_transactions

| Column Name      | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| investor_id      | TEXT      | Investor identifier        |
| transaction_date | DATE      | Transaction date           |
| amfi_code        | INTEGER   | Fund code                  |
| transaction_type | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr       | REAL      | Transaction amount         |
| state            | TEXT      | Investor state             |
| city             | TEXT      | Investor city              |
| age_group        | TEXT      | Investor age category      |
| gender           | TEXT      | Investor gender            |
| kyc_status       | TEXT      | KYC verification status    |

---

## fact_performance

| Column Name      | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| amfi_code        | INTEGER   | Fund code               |
| return_1yr_pct   | REAL      | 1-Year return           |
| return_3yr_pct   | REAL      | 3-Year return           |
| return_5yr_pct   | REAL      | 5-Year return           |
| alpha            | REAL      | Alpha metric            |
| beta             | REAL      | Beta metric             |
| sharpe_ratio     | REAL      | Sharpe Ratio            |
| sortino_ratio    | REAL      | Sortino Ratio           |
| max_drawdown_pct | REAL      | Maximum Drawdown        |
| aum_crore        | REAL      | Assets Under Management |
