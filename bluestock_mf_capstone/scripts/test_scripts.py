import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

query = """
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
"""

df = pd.read_sql(query, conn)

print(df)