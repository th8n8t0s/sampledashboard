import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Sales Overview Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Overview Dashboard (Sample)")

# Simulated sales data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
regions = ["North", "South", "East", "West"]
data = {
    "Date": np.tile(dates, 4),
    "Region": np.repeat(regions, 12),
    "Sales": np.random.randint(1000, 5000, size=48)
}
df = pd.DataFrame(data)

# Filters
st.sidebar.header("🔎 Filters")
selected_regions = st.sidebar.multiselect("Select Region(s)", options=regions, default=regions)

df_filtered = df[df["Region"].isin(selected_regions)]

# Line chart
st.subheader("📈 Monthly Sales by Region")
sales_pivot = df_filtered.pivot(index="Date", columns="Region", values="Sales")
fig, ax = plt.subplots(figsize=(10, 4))
sales_pivot.plot(ax=ax)
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
st.pyplot(fig)

# Bar chart
st.subheader("📊 Total Sales by Region")
total_sales = df_filtered.groupby("Region")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(total_sales)

# Table
st.subheader("🧾 Raw Data Table")
st.dataframe(df_filtered.reset_index(drop=True))

# Download
csv = df_filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Filtered Data (CSV)",
    data=csv,
    file_name="sample_sales_data.csv",
    mime="text/csv"
)

st.markdown("""
---
✅ *This is a demonstration of a clean, customizable Streamlit dashboard with filters, visuals, and export options. Use this as a portfolio showcase or template.*
""")

