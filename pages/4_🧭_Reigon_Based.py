import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import math
import seaborn as sns

#basic importing
df = pd.read_csv("dataset.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Date"] = pd.to_datetime(df["Order Date"]).dt.date
df["Month"] = df["Order Date"].dt.strftime('%B')
df["Year"] = df["Order Date"].dt.year

st.set_page_config(page_icon="🧭",page_title="Reigon Based",layout="wide")
st.header("Reigon Based Anaylsis 🗽")
st.subheader("Basic Analysis by Reigon and Comparisons...")  
st.sidebar.success("Select Pages From Above.")

st.markdown("")
st.markdown("")

st.markdown("### Sales by Cities:")
df["City"].value_counts().plot(kind="bar")
plt.title("Histogram of Cities")
plt.xlabel("City")
plt.ylabel("Count")
st.pyplot(plt.gcf())

st.markdown("")
st.markdown("")

st.markdown("### Sales by Region:")
cl1,cl2 =st.columns(2,gap="large")
region = df.pivot_table(index = 'Region', values = 'Sales', aggfunc = 'sum').reset_index().sort_values(by = 'Sales', ascending = False)
cl1.dataframe(region)
sns.barplot(x = 'Region', y = 'Sales', data = region)
plt.title('Total Sales by Region', fontsize = 14)
plt.tick_params(left= False, bottom = False, labelbottom = True)
plt.ylabel(None)
cl2.pyplot(plt.gcf())

st.markdown("")
st.markdown("")

st.markdown("### Sales by Region(Bar Plot):")
plt.figure(figsize=(5,3))
sns.boxplot(data=df, x="Sales", y="Region" , dodge=False )
cl3,cl4 =st.columns(2)
cl3.pyplot(plt.gcf())


