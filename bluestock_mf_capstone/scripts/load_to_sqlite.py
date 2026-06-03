from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

processed_dir = PROJECT_ROOT / "data" / "processed"
db_dir = PROJECT_ROOT / "data" / "db"

db_dir.mkdir(exist_ok=True)

db_path = db_dir / "bluestock_mf.db"

# SQLite connection
engine = create_engine(f"sqlite:///{db_path}")

# Load cleaned datasets
nav = pd.read_csv(
    processed_dir / "clean_nav_history.csv"
)

transactions = pd.read_csv(
    processed_dir / "clean_investor_transactions.csv"
)

performance = pd.read_csv(
    processed_dir / "clean_scheme_performance.csv"
)

fund_master = pd.read_csv(
    PROJECT_ROOT / "data" / "raw" / "01_fund_master.csv"
)

aum = pd.read_csv(
    PROJECT_ROOT / "data" / "raw" / "03_aum_by_fund_house.csv"
)

# Save tables
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database created successfully!")
print(f"Database Location: {db_path}")