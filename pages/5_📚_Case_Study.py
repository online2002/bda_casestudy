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

st.set_page_config(page_icon="📚",page_title="Case Study",layout="wide")
st.header("Case_Study 📑")
# st.subheader("Best Decisions for better Sales Result Based on Anaylsis...")  
st.sidebar.success("Select Pages From Above.") 

# sales_date=df.groupby("Order Date")["Sales"].sum()
# sales_date.plot(kind='line')
# st.pyplot(plt.gcf())
st.markdown("")

st.markdown("### Basic Suggetions from Analysis: (for better Sales Result)")
st.markdown("1. Discount in Order Increases the Sales.")
st.markdown("2. Beverages and Food Grains are the most Sold Item Category, discount or new product will help the sales.")
st.markdown("3. North Region need more branches to perform better.")
st.markdown("4. Metro cities have more potential to Sales.")
st.markdown("5. End of the year has shown more sales, new product line or discount can increase sales further.")


st.markdown("")
st.markdown("")

st.markdown("### Some unusal pattern after deep analysis:")
st.markdown("* there was a unusal behavior in sale in year 2016-17. The Annual year 2016 to 2017 has seen 23\% improvement in order placement, lets see the reasons...")
df_year = df[["Year"]]
df_year_orders_dict = df_year.value_counts().to_dict()
df_year_orders = pd.DataFrame(columns=["Year", "Orders Count"])
years = []
ordersCount = []

for key, value in df_year_orders_dict.items():
    years.append(int(''.join(map(str, key))))
    ordersCount.append(value)

df_year_orders["Year"] = years
df_year_orders["Orders Count"] = ordersCount

df_year_orders = df_year_orders.sort_values("Year", ascending=True)
df_year_orders = df_year_orders.reset_index(drop=True)
# st.dataframe(df_year_orders)

df_year_orders["Year-to-Year"] = ""
df_year_orders["Percentage_Growth"] = ""

year_to_year = []
percentage_growth_year_to_year = []

for i, current_row in df_year_orders.iterrows():
    previous_row = df_year_orders.shift(1).iloc[i]
    previous_year = previous_row["Year"]
    
    if math.isnan(previous_year):
        year_to_year.append("-2015")
        percentage_growth_year_to_year.append(0)
    else:
        year_to_year.append(str(int(previous_year)) + "-" + str(int(current_row["Year"])))
        
        previous_orders_count = previous_row["Orders Count"]
        current_orders_count = current_row["Orders Count"]
        percentage_growth = ((current_orders_count-previous_orders_count) / (previous_orders_count)) * 100
        percentage_growth_year_to_year.append(percentage_growth)

df_year_orders["Year-to-Year"] = year_to_year
df_year_orders["Percentage_Growth"] = percentage_growth_year_to_year
st.markdown("")
cl1,cl2 = st.columns(2,gap="large")
cl1.dataframe(df_year_orders,use_container_width=True)

plt.plot(df_year_orders["Year-to-Year"].tolist(), df_year_orders["Percentage_Growth"].tolist())
plt.xlabel("Year-to-Year")
plt.ylabel("Percentage_Growth")
plt.title("Performance of the order purchases over the year")
cl2.pyplot(plt.gcf())

st.markdown("### Difference In Sales of 2016-17 by Category:")

cl3,cl4 = st.columns(2,gap="large")
df_2016_2017 = df.loc[(df['Year'] == 2016) | (df['Year'] == 2017)]
df_2016_2017_Category = df_2016_2017.groupby('Year')['Category'].value_counts().reset_index(name='Count')
df_2016_2017_Category = df_2016_2017_Category.pivot(index="Category", columns='Year', values='Count').reset_index()
df_2016_2017_Category.columns = ['Category', '2016', '2017']
cl3.dataframe(df_2016_2017_Category,use_container_width=True)


growth_percentage_between_2016_and_2017 = [round((y2-y1)/y1*100, 2) 
                                           for y1, y2 in zip(df_2016_2017_Category["2016"].tolist(), 
                                                             df_2016_2017_Category["2017"].tolist())]
fig, ax = plt.subplots(figsize=(25,10))
ax.bar(df_2016_2017_Category["Category"].tolist(), growth_percentage_between_2016_and_2017)
ax.set_xlabel('Categories')
ax.set_ylabel('Percentage Growth (%)')
ax.set_title('Percentage Growth of Categories Between 2016 and 2017')
cl4.pyplot(plt.gcf())

st.markdown("> From abouve figure we can see -")
st.markdown("\t - Food Grains Category played a first major role in order purchases increased by 38.6%")
st.markdown("\t - Snacks Category played a second major role in order purchases increased by 28.85%")
st.markdown("\t - Oil & Masala Category played a third major role in order purchases increased by 28.37%")



st.markdown("### Role of Cities in Sudden Spike in Sale:")
st.markdown("")
df_2016_2017_Cities = df_2016_2017.groupby('Year')['City'].value_counts().reset_index(name='Count')
df_2016_2017_Cities = df_2016_2017_Cities.pivot(index="City", columns='Year', values='Count').reset_index()
df_2016_2017_Cities.columns = ['City', '2016', '2017']
growth_percentage_between_2016_and_2017 = [round((y2-y1)/y1*100, 2) 
                                           for y1, y2 in zip(df_2016_2017_Cities["2016"].tolist(), 
                                                             df_2016_2017_Cities["2017"].tolist())]
fig, ax = plt.subplots(figsize=(30,12))
ax.bar(df_2016_2017_Cities["City"].tolist(), growth_percentage_between_2016_and_2017)
ax.set_xlabel('Cities')
ax.set_ylabel('Percentage Growth (%)')
ax.set_title('Percentage Growth of Cities Between 2016 and 2017')
cl5,cl6 = st.columns(2,gap="large")
cl5.pyplot(plt.gcf())

cl6.markdown("> From the figure we can see -")
cl6.markdown("\t - Nagercoil has seen a drastic increase by 70.49/% in placing the orders")
cl6.markdown("\t - Namakkal has seen increase by 53.3/% increase in placing the orders")
cl6.markdown("\t - Tenkasi has seen increase by 43.75/% increase in placing the orders")
cl6.markdown("Bodi has seen a decline in the growth by 4.9%")


st.markdown("")
st.markdown("")
title_alignment="""
### <center>End.❤️+🔥=❤️‍🔥</center>
"""
st.markdown(title_alignment, unsafe_allow_html=True)