# %% [markdown]
# # MongoDB setup

# %% [markdown]
# ### Unzip

# %%
import py7zr

with py7zr.SevenZipFile('Dataset/US_youtube_trending_data.7z.', mode='r') as z:
    z.extractall()

# %% [markdown]
# #### Importing dependencies

# %%
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
client = MongoClient(host='localhost',port=27017)

# %%
client.list_database_names()

# %% [markdown]
# #### Creating database

# %%
db=client["bigdata"]

# %%
db.create_collection("videos")

# %%
db.list_collection_names()

# %%
videos=db["videos"]

# %% [markdown]
# ### Inseting data

# %%
videos_data_dict=pd.read_csv("US_youtube_trending_data.csv").to_dict(orient="records")
len(videos_data_dict)

# %%
os.remove("US_youtube_trending_data.csv")

# %%
videos.insert_many(videos_data_dict)

# %%
videos.count_documents({})

# %%
for i in videos.find({}).limit(3):
    print(i)


