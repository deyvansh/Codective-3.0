#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googleapiclient.discovery import build

def fetch_youtube_videos(api_key, query, max_results=5):
    """
    Fetch YouTube videos based on a search query.
    Returns: List of dictionaries with video title, URL, and thumbnail.
    """
    youtube = build('youtube', 'v3', developerKey='AIzaSyDyQg3Yom5ttD82Yy82mUJVnopJQH7YYnU')

    try:
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results,
            order='relevance'  # Sort by relevance
        )
        response = request.execute()

        videos = []
        for item in response['items']:
            video_id = item['id']['videoId']
            videos.append({
                'title': item['snippet']['title'],
                'url': f'https://www.youtube.com/watch?v={video_id}',
                'thumbnail': item['snippet']['thumbnails']['default']['url']
            })
        return videos

    except Exception as e:
        print(f"YouTube API Error: {e}")
        return []


# In[ ]:




