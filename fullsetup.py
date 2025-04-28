#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from aloo import fetch_youtube_videos
#from ipynb.fs.full. datasets import combined
from ipynb.fs.full. preprocessing import *


# In[2]:


@st.cache_data
def load_data_and_model():
    df = pd.read_csv("data/processed_data.csv")
    tfidf = joblib.load("models/tfidf_vectorizer.pkl")
    tfidf_matrix = joblib.load("models/tfidf_matrix.pkl") 
    return df, tfidf, tfidf_matrix

df, tfidf, tfidf_matrix = load_data_and_model()


# In[3]:


st.title("📚 Learning Resource Recommender")
st.markdown("Discover courses, books, and videos tailored to your interests!")
user_query = st.text_input("🔍 Enter a topic (e.g., Python, Machine Learning):", "Python")


# In[4]:


if user_query:
    # transform query into TF-IDF vector
    query_vector = tfidf.transform([user_query])

    # similarity scores
    cosine_sim = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # top 5 recommendations
    top_indices = cosine_sim.argsort()[-5:][::-1]
    content_recs = df.iloc[top_indices][['title', 'tag', 'url']]

    # results
    st.subheader("Recommended Courses & Books")
    for _, row in content_recs.iterrows():
        st.markdown(f"[{row['title']} ({row['tag']})]({row['url']})")


# In[5]:


# youtube videos
youtube_recs = fetch_youtube_videos(
    api_key=["AIzaSyDyQg3Yom5ttD82Yy82mUJVnopJQH7YYnU"],
    query=user_query,
    max_results=5
)

# YouTube results
st.subheader("Recommended YouTube Videos")
if youtube_recs:
    for video in youtube_recs:
        st.markdown(f"[{video['title']}]({video['url']})")
else:
    st.warning("No YouTube videos found.")


# In[ ]:




