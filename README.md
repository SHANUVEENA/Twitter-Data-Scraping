# Twitter-Data-Scraping
This project scrapes the Twitter data using Python Snscrape Library and package and export it to the MongoDB DataBase


pip install snscrape # Installing Snsrape

#Importing Library and Pacakges
import snscrape.modules.twitter as sntwitter 
import pandas as pd

username = input('Enter Your Keyword: ') #Username of the Twitter
number = int(input()) #Maximum no of Tweets Required

tweet_data = [] #Created list to Append Tweets Data

# Using TwitterSearchScraper to scrape data 
for i,tweets in enumerate(sntwitter.TwitterSearchScraper('{}'.format(username)).get_items()):
  if i>number:
    break
#Appending the Tweets data to Created list
  tweet_data.append([tweets.date, tweets.id, tweets.url, tweets.content, tweets.user.username, tweets.replyCount, tweets.retweetCount, tweets.lang, tweets.source, tweets.likeCount,   ])

# Creating a dataframe from the tweets list
df = pd.DataFrame(tweet_data, columns=['Date', 'ID', 'Url', 'Tweet_Content', 'Username',  'Reply_Count', 'Retweet_Count', 'Language', 'Source', 'Like_Count'])

#Displaying the dataframe
display(df) 

# Converting the dataframe into a dictionary
data = df.to_dict(orient = 'records') 

# Importing pymongo package
import pymongo

#Creating the connection between python and Mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

# Defining Database name
db = client["Twitter_date"]

print(db)

# Calling the Timestmap
from datetime import datetime
date_time = datetime.now().strftime("%d_%m_%y_%I_%M_%S_%p")
print("Twitter_data_" + date_time)

# Calling the connection
db.Twitter_data_26_01_23_05_06_53_PM.insert_many(data)
