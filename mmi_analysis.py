import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

plt.style.use("seaborn-v0_8")
pd.set_option("display.max_columns", None)

# ==============================
# LOAD DATA
# ==============================

file_path = "MMI_12-Mar-2025.csv"   # change to your file
df = pd.read_csv(file_path)


df.columns = ["Date", "MMI", "Nifty"]
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date").reset_index(drop=True)

# ==============================
# RETURNS CALCULATION
# ==============================

df["Daily_Return"] = df["Nifty"].pct_change()

# Forward returns
for days in [5, 10, 20, 60]:
    df[f"Fwd_{days}d_Return"] = df["Nifty"].shift(-days) / df["Nifty"] - 1

# ==============================
# CORRELATION ANALYSIS
# ==============================

print("\n==== Correlation Analysis ====")

for days in [5, 10, 20, 60]:
    valid = df[["MMI", f"Fwd_{days}d_Return"]].dropna()
    corr, p = pearsonr(valid["MMI"], valid[f"Fwd_{days}d_Return"])

    print(f"MMI vs {days}d Forward Return: Corr = {corr:.4f}, p-value = {p:.4f}")

# ==============================
# QUANTILE ANALYSIS
# ==============================

df["MMI_Quantile"] = pd.qcut(df["MMI"], 5, labels=False)

quantile_analysis = df.groupby("MMI_Quantile")[["Fwd_5d_Return",
                                                "Fwd_10d_Return",
                                                "Fwd_20d_Return",
                                                "Fwd_60d_Return"]].mean()

print("\n==== Quantile Forward Returns ====")
print(quantile_analysis)

# ==============================
# EXTREME FEAR & GREED STUDY
# ==============================

low_threshold = df["MMI"].quantile(0.2)
high_threshold = df["MMI"].quantile(0.8)

low_mmi = df[df["MMI"] <= low_threshold]
high_mmi = df[df["MMI"] >= high_threshold]

print("\n==== Extreme Fear (Lowest 20%) ====")
print(low_mmi[["Fwd_20d_Return", "Fwd_60d_Return"]].mean())

print("\n==== Extreme Greed (Highest 20%) ====")
print(high_mmi[["Fwd_20d_Return", "Fwd_60d_Return"]].mean())

# ==============================
# SIMPLE STRATEGY BACKTEST
# ==============================

# Strategy:
# Buy when MMI < 30
# Stay out when MMI > 70

df["Position"] = 0
df.loc[df["MMI"] < 30, "Position"] = 1
df.loc[df["MMI"] > 70, "Position"] = 0

df["Position"] = df["Position"].ffill()
df["Strategy_Return"] = df["Position"].shift(1) * df["Daily_Return"]

df["Buy_Hold"] = (1 + df["Daily_Return"]).cumprod()
df["Strategy"] = (1 + df["Strategy_Return"]).cumprod()

# ==============================
# PERFORMANCE METRICS
# ==============================

def performance_metrics(series):
    total_return = series.iloc[-1] - 1
    years = (df["Date"].iloc[-1] - df["Date"].iloc[0]).days / 365
    cagr = (series.iloc[-1])**(1/years) - 1
    return total_return, cagr

bh_total, bh_cagr = performance_metrics(df["Buy_Hold"])
st_total, st_cagr = performance_metrics(df["Strategy"])

print("\n==== Performance Comparison ====")
print(f"Buy & Hold Total Return: {bh_total:.2f}")
print(f"Buy & Hold CAGR: {bh_cagr:.2%}")
print(f"Strategy Total Return: {st_total:.2f}")
print(f"Strategy CAGR: {st_cagr:.2%}")

# ==============================
# VISUALIZATION
# ==============================

fig, axes = plt.subplots(3, 1, figsize=(12, 12))

axes[0].plot(df["Date"], df["MMI"])
axes[0].set_title("Market Mood Index Over Time")

axes[1].scatter(df["MMI"], df["Fwd_20d_Return"], alpha=0.4)
axes[1].set_title("MMI vs 20-Day Forward Return")

axes[2].plot(df["Date"], df["Buy_Hold"], label="Buy & Hold")
axes[2].plot(df["Date"], df["Strategy"], label="MMI Strategy")
axes[2].legend()
axes[2].set_title("Strategy vs Buy & Hold")

plt.tight_layout()
plt.show()
