# effort_calc.py - ETL cleanup rollout effort calculation

# Rerun this script after changing an estimate and it will recompute:
#   - base total: the sum of the four work-package estimates
#   - contingency: 15% on top of the base total
#   - grand total: base + contingency
#
# All numbers are rounded to one decimal place.

import pandas as pd

PACKAGES = [
    ("Audit ingestion scripts", 3),
    ("Rewrite validation layer", 5),
    ("Add integration tests", 8),
    ("Write the runbook", 2),
]

def main() -> None:
    df = pd.DataFrame(PACKAGES, columns=["package", "estimate"])
    base_total = round(df["estimate"].sum(), 1)
    contingency = round(base_total * 0.15, 1)
    grand_total = round(base_total + contingency, 1)
    print("ETL cleanup rollout - effort calculation")
    print("----------------------------------------")
    for _, row in df.iterrows():
        print(f"  {row['package']:<25} {row['estimate']:>4} person-days")
    print("----------------------------------------")
    print(f"Base total:    {base_total:.1f} person-days")
    print(f"Contingency:   {contingency:.1f} person-days (15% of base total)")
    print(f"Grand total:   {grand_total:.1f} person-days")


if __name__ == "__main__":
    main()