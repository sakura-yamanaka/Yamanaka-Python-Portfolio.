import streamlit as st
import pandas as pd

st.write("Hello homebuyers!")
st.title("Tallahassee Homes Explorer")
st.write("Find your dream home with this interactive app! Explore homes that fit your budget, ideal square footage, preferred bed/bath count, zip code, and year built.")

df = pd.read_csv("data/zillow.csv")

zipcode = st.selectbox("Select a Zipcode", df["Zip"].unique())
sqft = st.slider("Select Square Footage", min_value=int(df["Living Space (sq ft)"].min()), max_value=int(df["Living Space (sq ft)"].max()), value=int(df["Living Space (sq ft)"].mean()), step=100)
beds = st.slider("Select Number of Bedrooms", min_value=int(df["Beds"].min()), max_value=int(df["Beds"].max()), value=int(df["Beds"].mean()), step=1)
baths = st.slider("Select Number of Bathrooms", min_value=float(df["Baths"].min()), max_value=float(df["Baths"].max()), value=float(df["Baths"].mean()), step=0.5)
price = st.slider("Select List Price", min_value=int(df["List Price ($)"].min()), max_value=int(df["List Price ($)"].max()), value=int(df["List Price ($)"].mean()), step=5000)

filtered_df = df[
    (df["Zip"] == zipcode) &
    (df["Living Space (sq ft)"] >= sqft - 200) & (df["sqft"] <= sqft + 200) &
    (df["Beds"] == beds) &
    (df["Baths"] == baths) &
    (df["List Price ($)"] >= price - 5000) & (df["price"] <= price + 5000)
]

st.write(f"Homes that would be perfect for you:")
st.dataframe(filtered_df)
