import pandas as pd
import re
# --- Configuration ---
input_file = "data/tickets_clean.csv"
output_file = "data/tickets_clean.csv"
columns_to_clean = ["Title"]
keywords_to_remove = [""]

df = pd.read_csv(input_file, encoding="latin1")

def remove_keywords(text, keywords):
    if pd.isna(text):
        return text
    for kw in keywords:
        text = re.sub(re.escape(kw), "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text

for col in columns_to_clean:
    df[col] = df[col].apply(lambda x: remove_keywords(x, keywords_to_remove))

df.to_csv(output_file, index=False)
print(f"Cleaned CSV saved to {output_file}")