# generate_data.py
import pandas as pd
import numpy as np
import os

def generate_waste_data(output_path="data/waste_data.csv"):
    np.random.seed(42)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    zones = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"]

    data = []
    base_means = {"Zone A": 25, "Zone B": 30, "Zone C": 22, "Zone D": 28, "Zone E": 24}

    for date in dates:
        for zone in zones:
            # simulate seasonal effect: higher waste in summer months (May-Aug)
            month = date.month
            seasonal_factor = 1.08 if month in (5,6,7,8) else 1.0
            # weekday effect: slightly higher on weekends
            weekday_factor = 1.05 if date.weekday() >= 5 else 1.0

            mean_val = base_means[zone] * seasonal_factor * weekday_factor
            waste = np.random.normal(loc=mean_val, scale=4.0)
            waste = max(waste, 2.0)  # enforce a minimum
            data.append([date.strftime("%Y-%m-%d"), zone, round(waste, 2)])

    df = pd.DataFrame(data, columns=["date", "zone", "waste_generated_kg"])
    df.to_csv(output_path, index=False)
    print(f"Dataset created: {output_path} (rows: {len(df)})")

if __name__ == "__main__":
    generate_waste_data()
