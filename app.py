import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title=
"Sales Dashboard",

page_icon="📊",

layout="wide"
)

st.markdown(
"""
<h1 style='text-align:center;
color:#4CAF50;'>
📊 Sales Performance Dashboard
</h1>
""",
unsafe_allow_html=True
)

data = pd.read_csv("sales_data.csv")

revenue = data["Revenue"].sum()
profit = data["Profit"].sum()
orders = data["Orders"].sum()

col1,col2,col3 = st.columns(3)

col1.markdown(
f"""
<div style="
background-color:#1E88E5;
padding:20px;
border-radius:10px;
text-align:center;
color:white;">

<h3>Revenue</h3>

<h2>₹{revenue}</h2>

</div>
""",
unsafe_allow_html=True
)

col2.markdown(
f"""
<div style="
background-color:#43A047;
padding:20px;
border-radius:10px;
text-align:center;
color:white;">

<h3>Profit</h3>

<h2>₹{profit}</h2>

</div>
""",
unsafe_allow_html=True
)

col3.markdown(
f"""
<div style="
background-color:#FB8C00;
padding:20px;
border-radius:10px;
text-align:center;
color:white;">

<h3>Orders</h3>

<h2>{orders}</h2>

</div>
""",
unsafe_allow_html=True
)

st.subheader(
    "Sales Data"
)

st.dataframe(data)

pie = px.pie(
data,
values="Revenue",
names="Region",
color_discrete_sequence=
px.colors.qualitative.Set3
)


trend = px.line(
data,
x="Date",
y="Revenue",
markers=True
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