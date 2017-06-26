
# coding: utf-8

# In[1]:

import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('/Users/mayurjain/Documents/Python Data Analysis Practice/ml-1m/users.dat',sep='::',header=None,names=unames)
rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('/Users/mayurjain/Documents/Python Data Analysis Practice/ml-1m/ratings.dat',sep='::',header=None,names=rnames)
mnames = ['movie_id','title','genres']
movies = pd.read_table('/Users/mayurjain/Documents/Python Data Analysis Practice/ml-1m/movies.dat',sep='::',header=None,names=mnames)


# In[2]:

ratings[:5]


# In[3]:

ratings


# In[4]:

#Merging the columns from different dataframe
data = pd.merge(pd.merge(ratings,users),movies)


# In[5]:

data.head()


# In[6]:

data.ix[0]


# In[10]:

mean_ratings = data.pivot_table('rating', index='title',columns='gender',aggfunc='mean')
mean_ratings[:5]


# In[11]:

ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]


# In[12]:

active_titles = ratings_by_title.index[ratings_by_title>= 250]
active_titles


# In[13]:

mean_ratings = mean_ratings.ix[active_titles]
mean_ratings


# In[14]:

top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings[:10]


# In[15]:

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:15]


# In[16]:

#reversing the diff rating
sorted_by_diff[::-1][:15]


# In[20]:

rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title.head()


# In[21]:

rating_std_by_title = rating_std_by_title[active_titles]
rating_std_by_title.head()


# In[23]:

type(rating_std_by_title)


# In[ ]:



