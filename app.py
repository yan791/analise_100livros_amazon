import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top_100_books["book price"].max()
price_min = df_top_100_books["book price"].min()

max_price = st.sidebar.slider("Price Range ", price_min , price_max, price_max)
df_books = df_top_100_books[df_top_100_books["book price"]<= max_price]
df_books 
col1, col2 = st.columns(2)
fig = px.bar(df_top_100_books["year of publication"].value_counts()) 
col1.plotly_chart(fig)

fig2 = px.histogram(df_books["book price"])
col2.plotly_chart(fig2)
