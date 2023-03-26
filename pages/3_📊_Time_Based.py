import streamlit as st
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#basic importing
df = pd.read_csv("dataset.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Date"] = pd.to_datetime(df["Order Date"]).dt.date
df["Month"] = df["Order Date"].dt.strftime('%B')
df["Year"] = df["Order Date"].dt.year

st.set_page_config(page_icon="📊",page_title="Time Based",layout="wide")
st.header("Time Based Analysis⌛")
st.subheader("Basic Anaylsis Based on Time Period like Months and Years...")  
st.sidebar.success("Select Pages From Above.")

st.markdown("")
st.markdown("")

st.markdown("### Sales made vs profit")
st.markdown("It Shows that More Sale Brings More Profit over time...")
df.plot(x='Sales',y='Profit',kind='scatter')
st.pyplot(plt.gcf())


st.markdown("")
st.markdown("")

st.markdown("### Year Prgress in Sales:")

cl1,cl2 = st.columns(2,gap="large")
df["Year"].value_counts().plot(kind="bar")
plt.title("Histogram of Years")
plt.xlabel("Year")
plt.ylabel("Count")
cl1.pyplot(plt.gcf())

cl2.dataframe(df["Year"].value_counts(),use_container_width=True)


st.markdown("")
st.markdown("")

st.markdown("### Most Sale By Month:")
st.markdown("1. November")
st.markdown("2. December")
st.markdown("3. September")
st.markdown("> as shown in graph")


df["Month"].value_counts().plot(kind="bar")
plt.title("Histogram of Months")
plt.xlabel("Month")
plt.ylabel("Count")
st.pyplot(plt.gcf())

category_months_counts_df = df.groupby('Month')['Category'].value_counts().reset_index(name='Count')
category_months_counts_df = category_months_counts_df.sort_values(by="Month", key=lambda x: pd.to_datetime(x, format='%B'))
plt.figure(figsize=(25, 10))
sns.histplot(data=category_months_counts_df, x="Month", hue="Category", weights="Count", multiple="dodge", binwidth=10)
st.pyplot(plt.gcf())




