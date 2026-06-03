from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

raw_dir = PROJECT_ROOT / "data" / "raw"
processed_dir = PROJECT_ROOT / "data" / "processed"

processed_dir.mkdir(exist_ok=True)

nav = pd.read_csv(raw_dir / "02_nav_history.csv")

print("Before Cleaning:", nav.shape)

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

# Forward fill
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

print("After Cleaning:", nav.shape)

nav.to_csv(
    processed_dir / "clean_nav_history.csv",
    index=False
)

# ==========================
# INVESTOR TRANSACTIONS
# ==========================

transactions = pd.read_csv(
    raw_dir / "08_investor_transactions.csv"
)

print("\nTransactions Before Cleaning:",
      transactions.shape)

# Convert date
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Standardise transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Validate amount > 0
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Remove duplicates
transactions = transactions.drop_duplicates()

print("\nTransaction Types:")
print(transactions["transaction_type"].value_counts())

print("\nKYC Status:")
print(transactions["kyc_status"].value_counts())

print("\nTransactions After Cleaning:",
      transactions.shape)

transactions.to_csv(
    processed_dir / "clean_investor_transactions.csv",
    index=False
)


# ==========================
# SCHEME PERFORMANCE
# ==========================

performance = pd.read_csv(
    raw_dir / "07_scheme_performance.csv"
)

print("\nPerformance Before Cleaning:",
      performance.shape)

# Validate returns are numeric

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Flag negative Sharpe ratios

negative_sharpe = performance[
    performance["sharpe_ratio"] < 0
]

print("\nNegative Sharpe Funds:",
      len(negative_sharpe))

# Check expense ratio range

invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1)
    |
    (performance["expense_ratio_pct"] > 2.5)
]

print(
    "\nFunds Outside Expense Ratio Range:",
    len(invalid_expense)
)

print(
    "\nPerformance After Cleaning:",
    performance.shape
)

performance.to_csv(
    processed_dir /
    "clean_scheme_performance.csv",
    index=False
)