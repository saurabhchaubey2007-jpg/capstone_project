from pathlib import Path
import pandas as pd

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

print("=" * 60)
print("BLUESTOCK MF DATA INGESTION")
print("=" * 60)

csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    try:

        df = pd.read_csv(file)

        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nDtypes:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:

        print(f"ERROR: {e}")