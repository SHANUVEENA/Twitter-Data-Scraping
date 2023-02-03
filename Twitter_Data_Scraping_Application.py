#Importing Streamit Library
import streamlit as st
import json
import pandas as pd
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

# Twitter Logo
st.image("https://logodix.com/logo/8578.png", width=200)

# Application Title
st.title("Twitter Data Scraping Web Application")

# Tag line
st.write(
    """This application helps us to Scrape the Twitter data by entering the Username, limiting the no of Tweets and Specifying the Date range.
    """
)

# Uploading Snscrape and Pandas Library
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Textbox to Username as Input
username = st.text_input('Username', '')

# Slider for to Limit No of Tweets need to be Scraped
number = st.slider("No of Tweets", 0, 10000)

#Created list to Append Tweets Data
tweet_data = [] 

# Using TwitterSearchScraper to scrape data
for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
  if i>number:
    break
#Appending the Tweets data to Created list
  tweet_data.append([tweets.date, tweets.id, tweets.url, tweets.content, tweets.user.username, tweets.replyCount, tweets.retweetCount, tweets.lang, tweets.source, tweets.likeCount,   ])

# Creating a dataframe from the tweets list
df = pd.DataFrame(tweet_data, columns=['Date', 'ID', 'Url', 'Tweet_Content', 'Username',  'Reply_Count', 'Retweet_Count', 'Language', 'Source', 'Like_Count'])

df["Date"] =pd.to_datetime(df["Date"])

# Input text box to mention Date range
first_date = st.text_input('First Date (eg: YYYY-MM-DD)', '')
last_date = st.text_input('Last Date (eg: YYYY-MM-DD)', '')

df = df[df["Date"].between(first_date,last_date)]

st.dataframe(df)

# Converting the Dataframe into CSV
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

# CSV File Download button
st.download_button(
   "Download CSV",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

# Json File Download Button
json = df.to_json()
st.download_button(
   "Download JSON",
   json,
   "file.json",
   "text/json",
   key='download-json'
)

# Creating the Connection between python and MongoDB
data = df.to_dict(orient = 'records')
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Twitter_data"]
print(db)

#Impoting the Dataframe into DataBase by Clicking the Button
if st.button('Upload to DataBase'):
    db.Twitter_raw_data.insert_many(data)
