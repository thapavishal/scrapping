#!/usr/bin/env python
# coding: utf-8

# In[191]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[192]:


url = BeautifulSoup('https://www.worldometers.info/coronavirus/#countries', 'html.parser')
response = requests.get(url)
print(response)


# In[190]:


data = response.text
#print(data)
#data
soup = BeautifulSoup(data, 'lxml')
print(soup)


# In[193]:


get_table = soup.find("table",id="main_table_countries_today")
#get_table
get_table_data = get_table.tbody.find_all("tr")
#get_table_data


# In[194]:


dict = {}

#n = len(get_table_data)
#print(n)
for i in range(len(get_table_data)):
    try:
        key = get_table_data[i].find_all("a",href= True)[0].string
    except:
        key = get_table_data[i].find_all("td")[0].string
    #print(key)
    # list comprehension -> helps to write python code in single line
    values = [j.string for j in get_table_data[i].find_all('td')]
    
    dict[key] = values
#print(dict)  
#pd.DataFrame(dict)
column_names = ["TotalCases","New Cases","TotalDeaths", "New Deaths","TotalRecovered","Active Cases","Serious","Tot Cases/1M pop","Deaths/1M pop","Total Tests","Tests/1M pop", "Population"]
df = pd.DataFrame(dict).iloc[2:,1:].T.iloc[:,:12]
df


# In[195]:


df.index_name = "country"
df.columns = column_names
df


# In[196]:


df.to_csv("coronaVirus_cases.csv")


# In[197]:


df = pd.read_csv('coronaVirus_cases.csv', index_col=0)
df.head(20)


# In[198]:


import matplotlib.pyplot as plt


# In[199]:


x = df['TotalCases'].iloc[0:20].values
#print(x)
y = df['TotalDeaths'].iloc[0:20].values
#print(y)


# In[201]:


from matplotlib import style 
style.use("ggplot")
plt.figure(figsize=(16,9))
plt.title("Bar chart", fontsize = 18)
plt.xlabel("Total Cases", fontsize = 15)
plt.ylabel("Total Deaths", fontsize = 15)
plt.bar(x,y)

plt.show()


# In[ ]:




