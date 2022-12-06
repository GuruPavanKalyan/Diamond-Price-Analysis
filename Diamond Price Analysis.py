#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("C:/pandas/diamonds.csv")
print(data.head())


# In[5]:


#this data set contains unnamed column I want to delete it
#data = data.drop("Unnamed: 0",axis=1)
print(data.head())


# In[23]:


#price analysis between carat abd price
figure = px.scatter(data_frame = data, x="carat",
                    y="price", size="depth", 
                    color= "cut", trendline="ols")


# In[24]:


figure.show()


# In[25]:


#I want to find the realtionship between size and price
# creating size column
data["size"]=data["x"] * data["y"] * data["z"]
print(data)


# In[27]:


figure = px.scatter(data_frame = data, x="size",
                    y="price", size="depth", 
                    color= "cut", trendline="ols")
figure.show()


# In[28]:


# Prices of all the types of diamonds based on their colour
fig = px.box(data, x="cut", 
             y="price", 
             color="color")
fig.show()


# In[29]:


#checking correlation
correlation = data.corr()
print(correlation["price"].sort_values(ascending=False))


# In[ ]:




