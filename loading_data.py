# %% [markdown]
# # MongoDB setup

# %% [markdown]
# ### Unzip

# %%

print("Unzipping file")
import py7zr

with py7zr.SevenZipFile('Dataset/US_youtube_trending_data.7z', mode='r') as z:
    z.extractall()

print("Extracted data")

# %% [markdown]
# #### Importing dependencies

# %%
print("***********************************************")
print("\n Loading Dependenceis")
import os
import pprint
import pandas as pd
from pymongo import MongoClient
import pprint

# %%
# !pip freeze > requirements.txt

# %% [markdown]
# ### Databasse information
# 
# database name : bigdata  
# collection name: videos

# %%
print("***********************************************")
print("\n Connecting to db")
client = MongoClient(host='localhost',port=27017)
print(f"Connection established :{client.HOST}")
# %%
print(client.list_database_names())

# %% [markdown]
# #### Creating database

# %%
print("***********************************************")
print("\n creating database")
db=client["bigdata"]
print("database created")
# %%
print("creating collections")
db.create_collection("videos")
print("collection created")

# %%
print(db.list_collection_names())

# %%
videos=db["videos"]

# %% [markdown]
# ### Inseting data

# %%
print("Loading csv")
videos_data_dict=pd.read_csv("US_youtube_trending_data.csv").to_dict(orient="records")
# videos.groupby("")
print(len(videos_data_dict))

# %%
os.remove("US_youtube_trending_data.csv")

# %%

print("add data")
videos.insert_many(videos_data_dict)

# %%
print(videos.count_documents({}))

# %%
for i in videos.find({}).limit(3):
    print(i)
print("!Done")

