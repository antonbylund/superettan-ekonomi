# scripts/extract_financials.py

import pdfplumber
import os
import re
import pandas as pd

raw_path = "data/raw/2024"
output_path = "data/processed/finances_2024.csv"

data = []

def extract_numbers(text):
    match = re.search(r'(\d[\d\s]+)', text.replace('.', '').replace(',', ''))
    if match:
        return int(match.group(1).replace(' ', ''))
    return None

for file in os.listdir(raw_path):
    if file.endswith(".pdf"):
        club_name = file.replace(".pdf", "").replace("_", " ").title()
        pdf_path = os.path.join(raw_path, file)
        with pdfplumber.open(pdf_path) as pdf:
            full_text = "\n".join(p.extract_text() or "" for p in pdf.pages)
            revenue = extract_numbers(re.search(r"(omsättning|intäkter).{0,30}(\d[\d\s]+)", full_text.lower()).group(2)) if re.search(r"(omsättning|intäkter).{0,30}(\d[\d\s]+)", full_text.lower()) else None
            wages = extract_numbers(re.search(r"(personalkostnader).{0,30}(\d[\d\s]+)", full_text.lower()).group(2)) if re.search(r"(personalkostnader).{0,30}(\d[\d\s]+)", full_text.lower()) else None

            data.append({
                "club": club_name,
                "revenue_total": revenue,
                "wage_costs": wages
            })

df = pd.DataFrame(data)
df.to_csv(output_path, index=False)
print("✅ Data sparad till:", output_path)
