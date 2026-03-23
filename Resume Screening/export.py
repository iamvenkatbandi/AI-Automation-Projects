import pandas as pd
import os

def export_to_csv(data):
    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv("output/results.csv", index=False)

    print("✅ Results saved to output/results.csv")
