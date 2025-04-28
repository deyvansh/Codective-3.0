

import streamlit as st
import joblib
from ipynb.fs.full. aloo import fetch_youtube_videos



# Streamlit UI
st.title("Learning Recommender System")
user_query = st.text_input("Search for a topic (e.g., Python):")

if user_query:
    #  Content-based recommendations (courses/books)
    
    #  Fetch YouTube videos
    youtube_videos = fetch_youtube_videos(
        api_key="AIzaSyDyQg3Yom5ttD82Yy82mUJVnopJQH7YYnU",  # Replace with your key
        query=user_query,
        max_results=5
    )

    # Display results
    st.subheader("Recommended Courses/Books:")
    # ... (display courses/books)

    st.subheader("Recommended YouTube Videos:")
    if youtube_videos:
        for video in youtube_videos:
            st.markdown(f"[{video['title']}]({video['url']})")
            st.image(video['thumbnail'])  # Optional: Show thumbnail
    else:
        st.write("No videos found. Try another topic!")






