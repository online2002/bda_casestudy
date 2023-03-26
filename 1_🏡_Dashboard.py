from PIL import Image
import pandas as pd
import streamlit as st
from plotly import express as px

df = pd.read_csv("dataset.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Date"] = pd.to_datetime(df["Order Date"]).dt.date
df["Month"] = df["Order Date"].dt.strftime('%B')
df["Year"] = df["Order Date"].dt.year



st.set_page_config(page_icon="🛒",page_title="Dmart Case-Study",layout="wide")
st.header("DashBoard ✌️")
st.subheader("Basic D-Mart Sales Analysis")  
st.sidebar.success("Select Pages From Above.")

total_sale = int(df["Sales"].sum())
# st.markdown(total_sale)
average_sale_per_month = int(round(df["Sales"].mean(),2)*30)
# st.markdown(average_sale_per_day)

st.markdown("")
st.markdown("")

lc,rc = st.columns(2)
with lc:
    st.subheader("Total Sales:")
    st.subheader(f"₹{total_sale:,}")
with rc:
    st.subheader("Average Sales Per Month:")
    st.subheader(f"₹{average_sale_per_month:,}")

#bar_Chart
st.markdown("")
st.markdown("")

date = df["Date"].unique().tolist()
sales = df["Sales"].tolist()
city = df["City"].sort_values(ascending=True).unique().tolist()

date_selection = st.slider("Date:",
                           min_value=min(date),
                           max_value=max(date),
                           value=(min(date),max(date)))

city_select = st.multiselect("Cities:",
                             city,default=city)



mask = (df["Order Date"].isin(pd.date_range(min(date_selection),max(date_selection)))) & (df["City"].isin(city_select))
nor = df[mask].shape[0]
st.markdown(f'*Availabel result: {nor}*')

df_group = df[mask].groupby(by=["City"]).count()[["Date"]]
df_group = df_group.rename(columns={"Date" : "Sales"})
df_group = df_group.reset_index()
if(nor!=0):
    bar_chart = px.bar(df_group,x="City",y='Sales',
                    text='Sales',
                    color_discrete_sequence= ['#F63366']*len(df_group),
                    template='plotly_white')
    st.plotly_chart(bar_chart,use_container_width=True)


st.markdown("")
st.markdown("")

cl1,cl2 =st.columns(2)
img1 = Image.open('images/one.png')
cl1.image(img1)
cl2.dataframe(df)

# df["Date"].sort_values(ascending=True).unique().tolist()

st.markdown("")
st.markdown("")

cl3,cl4 = st.columns(2,gap="large")
img2 = Image.open('images/three.png')
cl4.image(img2)
pie_chart1 = px.pie(df,title="Yearly Sale",
                   values='Sales',
                   names='Year')
cl3.plotly_chart(pie_chart1,use_container_width=True)

st.markdown("")
st.markdown("")

cl5,cl6 = st.columns(2,gap="large")
img3 = Image.open('images/four.png')
cl5.image(img3)
pie_chart2 = px.pie(df,title="Monthly Sale",
                   values='Sales',
                   names=df["Month"])
cl6.plotly_chart(pie_chart2,use_container_width=True)

st.markdown("")
st.markdown("")

cl7,cl8 = st.columns(2,gap="large")
img4 = Image.open('images/two.png')
cl8.image(img4)
pie_chart3 = px.pie(df,title="Cities",
                   values='Sales',
                   names='City')

cl7.plotly_chart(pie_chart3,use_container_width=True)