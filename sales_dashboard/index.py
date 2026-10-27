import pandas as pd

# ============================================
# 1. LOAD DATA
# ============================================

# Read CSV file
# parse_dates converts the "date" column into datetime format
df = pd.read_csv("sales.csv", parse_dates=["date"])


# ============================================
# 2. CLEAN DATA
# ============================================

# Remove rows where amount or region is missing
df = df.dropna(subset=["amount", "region"])

# Clean region names
# "  north " -> "North"
# "south"    -> "South"
# "EAST"     -> "East"
df["region"] = df["region"].str.strip().str.title()

# Convert amount into numeric values
# Invalid values become NaN
df["amount"] = pd.to_numeric(
    df["amount"],
    errors="coerce"
)

# Remove rows where amount could not be converted to a number
df = df.dropna(subset=["amount"])


# ============================================
# 3. HEADLINE METRICS
# ============================================

# Total revenue
total_revenue = df["amount"].sum()

# Total units sold
units_sold = df["quantity"].sum()

# Average order value
avg_order = df["amount"].mean()

# Display headline metrics
print("\n========== HEADLINE METRICS ==========")

print(
    f"Revenue: {total_revenue:,.0f} | "
    f"Units: {units_sold} | "
    f"AOV: {avg_order:,.1f}"
)


# ============================================
# 4. REVENUE BY REGION
# ============================================

by_region = (
    df.groupby("region")["amount"]
      .sum()
      .sort_values(ascending=False)
)

print("\n========== REVENUE BY REGION ==========")

print(by_region)


# ============================================
# 5. TOP 5 PRODUCTS
# ============================================

top_products = (
    df.groupby("product")["amount"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

print("\n========== TOP 5 PRODUCTS ==========")

print(top_products)


# ============================================
# 6. MONTHLY REVENUE TREND
# ============================================

monthly = (
    df.set_index("date")["amount"]
      .resample("ME")
      .sum()
)

print("\n========== MONTHLY REVENUE ==========")

print(monthly)