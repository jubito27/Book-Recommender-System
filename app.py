import pickle
import streamlit as st

df = pickle.load(open(r'C:\Users\Abhishek sharma\Artificial Intelligence\Machine Learning\Projects\Books Recommender\top_50_data' , 'rb'))
df = df.drop(columns=['ISBN' , 'User-ID'])

st.title("Books Recommender System")
st.subheader("Top 50 books")

st.dataframe(df)
