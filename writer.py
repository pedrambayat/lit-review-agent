import pandas as pd
import os

def save_to_csv(papers, filename="results.csv"):
    df = pd.DataFrame(papers)
    os.makedirs("output", exist_ok=True)
    df.to_csv(os.path.join("output", filename), index=False)
