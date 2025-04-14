import streamlit as st
import pandas as pd

st.title("Tallahassee Homes Explorer")
st.subheader("Hello homebuyers!")
st.write("Find your dream home with this interactive app! Explore homes that fit your budget, ideal square footage, preferred bed/bath count, and zip code.")

import os
df = pd.read_csv(os.path.abspath("/Users/sakurayamanaka/Documents/Yamanaka-Python-Portfolio./basic_streamlit_app/data/zillow.csv"))

zipcode = st.selectbox("Select a Zipcode", df["Zip"].unique())
sqft = st.slider("Select Square Footage", min_value=int(df["Living Space (sq ft)"].min()), max_value=int(df["Living Space (sq ft)"].max()), value=int(df["Living Space (sq ft)"].mean()), step=100)
beds = st.slider("Select Number of Bedrooms", min_value=int(df["Beds"].min()), max_value=int(df["Beds"].max()), value=int(df["Beds"].mean()), step=1)
baths = st.slider("Select Number of Bathrooms", min_value=int(df["Baths"].min()), max_value=int(df["Baths"].max()), value=int(df["Baths"].mean()), step=1)
price = st.slider("Select List Price", min_value=int(df["List Price ($)"].min()), max_value=int(df["List Price ($)"].max()), value=int(df["List Price ($)"].mean()), step=5000)

filtered_df = df[
    (df["Zip"] == zipcode) &
    (df["Living Space (sq ft)"] >= sqft - 200) & (df["Living Space (sq ft)"] <= sqft + 200) &
    (df["Beds"] == beds) &
    (df["Baths"] == baths) &
    (df["List Price ($)"] >= price - 5000) & (df["List Price ($)"] <= price + 5000)
]

filtered_df2 = df[
    (df["Living Space (sq ft)"] >= sqft - 500) & (df["Living Space (sq ft)"] <= sqft + 500) &
    (df["Beds"] <= beds) &
    (df["Baths"] <= baths) &
    (df["List Price ($)"] >= price - 10000) & (df["List Price ($)"] <= price + 10000)
]

st.write(f"Homes that would be perfect for you:")
st.dataframe(filtered_df)

st.write(f"Homes that are (almost!) perfect for you:")
st.dataframe(filtered_df)