import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load files
cleaned_data = pd.read_csv("cleaned_swiggy.csv")
encoded_data = pd.read_csv("encoded_data.csv")

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

st.title("🍽️ Swiggy Restaurant Recommendation System")
st.divider()

# User Inputs
city = st.selectbox("Select City", cleaned_data['city'].unique())
cuisine = st.selectbox("Select Cuisine", cleaned_data['cuisine'].unique())
rating = st.slider("Minimum Rating", 1.0, 5.0, 3.5)
cost = st.slider("Maximum Cost (₹)", 50, 1000, 300)

if st.button("Recommend Restaurants"):
    
    user_cat = encoder.transform([[city, cuisine]])
    user_vector = np.concatenate([[rating, 50, cost], user_cat[0]])
    
    similarity = cosine_similarity([user_vector], encoded_data)[0]
    top_indices = similarity.argsort()[::-1][:5]
    
    results = cleaned_data.iloc[top_indices]

    st.divider()

    st.subheader("Similarity Score")
    st.markdown(f"**Max similarity:** {similarity.max():.4f}")
    st.markdown(f"**Mean similarity:** {similarity.mean():.4f}")
    
    st.divider()

    st.subheader("Recommended Restaurants")
    st.dataframe(results[['name', 'city', 'cuisine', 'rating', 'cost']])
