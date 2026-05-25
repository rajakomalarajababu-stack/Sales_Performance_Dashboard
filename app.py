import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Performance Dashboard")

data = pd.read_csv("sales_data.csv")

revenue = data["Revenue"].sum()
profit = data["Profit"].sum()
orders = data["Orders"].sum()

col1,col2,col3 = st.columns(3)

col1.metric(
    "Revenue",
    f"₹{revenue}"
)

col2.metric(
    "Profit",
    f"₹{profit}"
)

col3.metric(
    "Orders",
    orders
)

st.subheader(
    "Sales Data"
)

st.dataframe(data)

fig = px.bar(
    data,
    x="Product",
    y="Revenue",
    color="Region",
    title="Revenue by Product"
)

st.plotly_chart(fig)

trend = px.line(
    data,
    x="Date",
    y="Revenue",
    title="Revenue Trend"
)

st.plotly_chart(trend)

region = px.pie(
    data,
    names="Region",
    values="Revenue",
    title="Region Revenue Share"
)

st.plotly_chart(region)

top = data.groupby(
    "Product"
)["Revenue"].sum()

st.write(
    "Top Product:",
    top.idxmax()
)
region = st.selectbox(
    "Select Region",
    data["Region"].unique()
)

filtered = data[
    data["Region"] == region
]

st.dataframe(filtered)
growth = (
    data["Revenue"]
    .pct_change()
    *100
)

st.line_chart(growth)
margin = (
profit/revenue
)*100

st.metric(
"Profit Margin",
f"{margin:.2f}%"
)