import requests
import pandas as pd
from pathlib import Path

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_dir = Path("data/raw")

for scheme_name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = output_dir / f"{scheme_name}_NAV.csv"

        df.to_csv(filename, index=False)

        print(f"✓ Saved {scheme_name}")

    else:

        print(f"✗ Failed {scheme_name}")