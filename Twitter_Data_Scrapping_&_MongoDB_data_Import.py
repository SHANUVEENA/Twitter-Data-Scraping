#!/usr/bin/env python
# coding: utf-8

# In[100]:


pip install snscrape


# In[101]:


import snscrape.modules.twitter as sntwitter 
import pandas as pd


# In[102]:


username = input('Enter Your Keyword: ')
number = int(input())

tweet_data = []


for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
  if i>number:
    break

  tweet_data.append([tweets.date, tweets.id, tweets.url, tweets.content, tweets.user.username, tweets.replyCount, tweets.retweetCount, tweets.lang, tweets.source, tweets.likeCount,   ])


df = pd.DataFrame(tweet_data, columns=['Date', 'ID', 'Url', 'Tweet_Content', 'Username',  'Reply_Count', 'Retweet_Count', 'Language', 'Source', 'Like_Count'])


# In[103]:


display(df)


# In[104]:


data = df.to_dict(orient = 'records')


# In[105]:


import pymongo


# In[106]:


client = pymongo.MongoClient("mongodb://localhost:27017")


# In[107]:


db = client["Twitter_date"]


# In[108]:


print(db)


# In[112]:


from datetime import datetime
date_time = datetime.now().strftime("%d_%m_%y_%I_%M_%S_%p")
print("Twitter_data_" + date_time)


# In[113]:


db.Twitter_data_26_01_23_05_06_53_PM.insert_many(data)

