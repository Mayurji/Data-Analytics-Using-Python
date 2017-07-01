
# coding: utf-8

# In[25]:

import quandl
import pandas as pd
import pickle

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandl.txt','r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        print(query)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,lsuffix=abbv)
            
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        

    
grab_initial_state_data()


# In[26]:

pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)


# In[27]:

HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)


# In[32]:

HPI_data2['TX2'] = HPI_data2['ValueTX'] * 2
print(HPI_data2[['ValueTX','TX2']].head())


# In[33]:

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# In[34]:

HPI_data2.plot()
plt.legend().remove()
plt.show()


# In[37]:

def grab_initial_state_data2():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        print(query)
        df = df.pct_change()
        #print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,lsuffix=abbv)
            
    pickle_out = open('fiddy_states2.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

grab_initial_state_data2()
HPI_datas = pd.read_pickle('fiddy_states2.pickle')

HPI_datas.plot()
plt.legend().remove()
plt.show()


# In[ ]:



