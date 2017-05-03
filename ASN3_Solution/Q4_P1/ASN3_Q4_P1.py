
# coding: utf-8

# # Q4_PART_ONE

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

data=pd.read_csv("movies_awards.csv",usecols=['Awards'])
#data.head()


# In[3]:

#Extracting awards won
data['Awards_won'] = data['Awards'].str.extract('(\d+\swin)', expand=True)
data['Awards_won'] = data['Awards_won'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

#Extractinng awards nominated
data['Awards_nominated'] = data['Awards'].str.extract('(\d+\snomination)', expand=True)
data['Awards_nominated'] = data['Awards_nominated'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)


#Extractinng Oscar awards won
data['Oscar_Awards_won'] = data['Awards'].str.extract('(Won\s\d+\sOscar)', expand=True)
data['Oscar_Awards_won'] = data['Oscar_Awards_won'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

#Extractinng Oscar awards nominated
data['Oscar_Awards_nominated'] = data['Awards'].str.extract('(Nominated\sfor\s\d+\sO)', expand=True)
data['Oscar_Awards_nominated'] = data['Oscar_Awards_nominated'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)


#Extractinng BAFTA  awards won
data['BAFTA_Awards_won'] = data['Awards'].str.extract('(Won\s\d+\sBAFTA)', expand=True)
data['BAFTA_Awards_won'] = data['BAFTA_Awards_won'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

#Extractinng BAFTA  awards nominated
data['BAFTA_Awards_nominated'] = data['Awards'].str.extract('(Nominated\sfor\s\d+\sBAFTA)', expand=True)
data['BAFTA_Awards_nominated'] = data['BAFTA_Awards_nominated'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

#Extractinng Golden Globe  awards won
data['Golden_Globe_Awards_won'] = data['Awards'].str.extract('(Won\s\d+\sG)', expand=True)
data['Golden_Globe_Awards_won'] = data['Golden_Globe_Awards_won'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

#Extractinng Golden Globe  awards nominated
data['Golden_Globe_Awards_nominated'] = data['Awards'].str.extract('(Nominated\sfor\s\d+\sG)', expand=True)
data['Golden_Globe_Awards_nominated'] = data['Golden_Globe_Awards_nominated'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)


#Extractinng Primetime Emmy awards won
data['Primetime_Emmy_Awards_won'] = data['Awards'].str.extract('(Won\s\d+\sP)', expand=True)
data['Primetime_Emmy_Awards_won'] = data['Primetime_Emmy_Awards_won'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)


#Extractinng Primetime Emmye  awards nominated
data['Primetime_Emmy_Awards_nominated'] = data['Awards'].str.extract('(Nominated\sfor\s\d+\sP)', expand=True)
data['Primetime_Emmy_Awards_nominated'] = data['Primetime_Emmy_Awards_nominated'].str.extract('(\d+)', expand=True).apply(pd.to_numeric)

data.head()


# In[4]:

#Converting all NaN award won and nominated columns to 0 and summing them up for final count

data =data.fillna(0)

data['Awards_won'] = data['Awards_won'] + data['Oscar_Awards_won'] + data['BAFTA_Awards_won']                    + data['Golden_Globe_Awards_won'] + data['Primetime_Emmy_Awards_won']
    
data['Awards_nominated'] = data['Awards_nominated'] + data['Oscar_Awards_nominated'] +                            data['BAFTA_Awards_nominated'] + data['Golden_Globe_Awards_nominated'] +                           data['Primetime_Emmy_Awards_nominated']
        
data = data[data.Awards != 0]      # Removing Awards column entry where there is no data      
data.head()


# In[5]:

data.to_csv('Q4_P1.csv',index=False, encoding='utf-8')   #Saving data to CSV file


# In[ ]:



