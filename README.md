
📊 Market Mood Index (MMI) Analysis on Nifty
============================================

A quantitative research project to evaluate whether the **Market Mood Index (MMI)** provides predictive insights for trading or investing in the Nifty Index.

*   Does MMI predict future Nifty returns?
*   Is MMI a contrarian indicator?
*   Can MMI improve performance vs Buy & Hold?
*   Do extreme fear/greed zones create opportunity?


📦 Requirements
---------------

pip install pandas numpy matplotlib seaborn scipy openpyxl

📊 Dataset Format
-----------------

Date Market Mood Index Nifty Index

11-03-2025 52.22 22497.9

**Notes:**

*   Date format: DD-MM-YYYY
*   Daily frequency
*   Supports .csv or .xlsx


🚀 How to Run
-------------

### 1️⃣ Update file path inside script

file\_path = "mmi\_data.csv"

### 2️⃣ Run the script

python mmi\_analysis.py


<img width="1501" height="1015" alt="image" src="https://github.com/user-attachments/assets/ba3dddb3-6e12-40ed-a2af-f0f82ebb5759" />

<img width="985" height="734" alt="image" src="https://github.com/user-attachments/assets/270b0c63-7ddb-4c55-bc19-3f6ec63313ee" />



🔬 Analysis Performed
---------------------

### 1️⃣ Forward Return Calculation

*   5-day forward return
*   10-day forward return
*   20-day forward return
*   60-day forward return

### 2️⃣ Correlation Analysis

*   Pearson correlation
*   Statistical significance (p-value)

### 3️⃣ Quantile Study

MMI divided into 5 buckets to analyze forward returns behavior.

### 4️⃣ Extreme Regime Study

*   Lowest 20% → Extreme Fear
*   Highest 20% → Extreme Greed

### 5️⃣ Strategy Backtest

Tested rule:

Buy when MMI < 30
Exit when MMI > 70

📈 Example Findings
-------------------

*   Very low linear correlation between MMI and future returns
*   No strong contrarian signal observed
*   Strategy underperformed Buy & Hold
*   MMI appears slightly pro-cyclical

**Conclusion:** MMI alone is not a strong standalone trading signal.

📊 Visual Output
----------------

*   MMI time series chart
*   Scatter plot (MMI vs forward returns)
*   Strategy vs Buy & Hold equity curve

🧠 Future Improvements
----------------------

*   Combine MMI with volatility index (VIX)
*   Use MMI as regime filter
*   Rolling window correlation
*   Machine learning prediction models
*   Dynamic threshold strategy

⚠️ Disclaimer
-------------

This project is for educational and research purposes only. It is not financial advice. Past performance does not guarantee future results.

