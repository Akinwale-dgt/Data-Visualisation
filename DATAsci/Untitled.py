#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd #load data
data = "../DATA VISUALIZATION/data.csv"
nam_of_data = pd.read_csv(data)
nam_of_data.head()  # top 5 rows


# In[13]:


nam_of_data.describe() # return statistic about the data


# In[14]:


nam_of_data.shape  # return number of row ans columns


# In[15]:


nam_of_data.columns # return nsme of columns


# In[16]:


# nam_of_data.columns= ["A,"B","C"]  # use A,B,C has the names of the column
nam_of_data.dtypes  # return the data type of each columns


# In[17]:


nam_of_data["temp"]= 0


# In[18]:


nam_of_data.head()


# In[19]:


nam_of_data["compute"] = nam_of_data["temp"]+nam_of_data['population']*nam_of_data["households"]


# In[20]:


nam_of_data.head()


# In[22]:


data_minor = nam_of_data[nam_of_data["housing_median_age"] <= 18]


# In[23]:


data_minor.describe()


# In[24]:


nam_of_data.plot()


# In[27]:


import matplotlib.pyplot as plt


# In[31]:


import os

os.system('git init')
os.system("git branch -a")
# os.system("git commit -m  pandas data")


# In[ ]:





# In[ ]:




