#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install snscrape


# In[2]:


import snscrape.modules.twitter as sntwitter 
import pandas as pd


# In[3]:


username = input('Enter Your Keyword: ')
number = int(input())

tweet_data = []


for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
  if i>number:
    break

  tweet_data.append([tweets.date, tweets.id, tweets.url, tweets.content, tweets.user.username, tweets.replyCount, tweets.retweetCount, tweets.lang, tweets.source, tweets.likeCount,   ])


df = pd.DataFrame(tweet_data, columns=['Date', 'ID', 'Url', 'Tweet_Content', 'Username',  'Reply_Count', 'Retweet_Count', 'Language', 'Source', 'Like_Count'])


# In[5]:


display(df)


# In[6]:


data = df.to_dict(orient = 'records')


# In[7]:


import pymongo


# In[8]:


client = pymongo.MongoClient("mongodb://localhost:27017")


# In[9]:


db = client["Twitter_date"]


# In[10]:


print(db)


# In[11]:


from datetime import datetime
date_time = datetime.now().strftime("%d_%m_%y_%I_%M_%S_%p")
print("Twitter_data_" + date_time)


# In[12]:


db.Twitter_data_03_02_23_01_38_20_PM.insert_many(data)


# In[ ]:




