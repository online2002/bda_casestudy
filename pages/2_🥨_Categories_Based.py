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

st.set_page_config(page_icon="🥨",page_title="Categories Based",layout="wide")
st.header("Categories Based Analysis 🧃")
st.subheader("Basic Categories like Foods & Beverages...")  
st.sidebar.success("Select Pages From Above.")

st.markdown("")
st.markdown("")

cl0,cl01 = st.columns(2,gap="small")
category = df.pivot_table(index = ['Category', 'Sub Category'], values = 'Sales', aggfunc = 'sum').reset_index().sort_values(by = 'Sales', ascending = False)
cl0.dataframe(category,use_container_width=True)

cl01.markdown("### **Dataset**")
cl01.markdown("Basic dataset of categories derived from sorting values and by reset indexing from main table...")

st.markdown("")
st.markdown("")

cl1,cl2 = st.columns(2,gap="large")
plt.rcParams['figure.figsize'] = (10,4)
sns.barplot(x = 'Category', y = 'Sales', data = category)
plt.title('Total Sales by Category', fontsize = 14)
plt.tick_params(left= False, bottom = False, labelbottom = True)
plt.ylabel(None)
cl2.pyplot(plt.gcf())

cl1.markdown("### **Conclusion**")
cl1.markdown("")
cl1.markdown("Most Sold items by category:")
cl1.markdown("1. Beverages")
cl1.markdown("2. Snacks")
cl1.markdown("3. Bakery")

st.markdown("")
st.markdown("")

cl3,cl4 = st.columns(2,gap="large")

plt.figure(figsize=(20,10))
sns.barplot(x = 'Sub Category', y = 'Sales', data = category)
plt.title('Total Sales by Sub Category', fontsize = 14)
plt.tick_params(left= True, bottom = False, labelbottom = True,)
plt.ylabel(None)
cl3.pyplot(plt.gcf())

cl4.markdown("### **Conclusion**")
cl4.markdown("")
cl4.markdown("Most Sold items by sub-category:")
cl4.markdown("- Health Drinks")
cl4.markdown("- Soft Drinks")
cl4.markdown("- Cookies")

st.markdown("")
st.markdown("")

cl5,cl6 = st.columns(2)

df["Category"].value_counts().plot(kind="bar")
plt.title("Histogram of Categories")
plt.xlabel("Category")
plt.ylabel("Count")
cl6.pyplot(plt.gcf())

cl5.dataframe(df["Category"].value_counts(),use_container_width=True)

st.markdown("")
st.markdown("")

st.markdown("### Comparision Between Two Most Sold Categories")
plt.figure(figsize=(10,4))
df[df["Category"]=='Beverages']["Sales"].hist(alpha=0.5,bins=20)
df[df["Category"]=='Food Grains']["Sales"].hist(alpha=0.5,bins=20)
plt.legend(['Beverages','Food Grains'])
st.pyplot(plt.gcf())

