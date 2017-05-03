
# coding: utf-8

# # Q2_PART_ONE

# In[1]:

import pandas as pd
import datetime as dt
import calendar


# In[46]:

main_data = pd.read_csv('employee_compensation.csv',usecols=['Organization Group','Department','Total Compensation']) 
#main_data.groupby('Department').mean()

department =main_data.Department.unique()            # Storing department name and organization group in list
org = main_data['Organization Group'].unique()


df_agg = main_data.groupby(['Organization Group','Department']).mean()    #calculating mean
df_agg = df_agg.reset_index()                                             #reseting index
df_agg=df_agg.sort_values(by='Total Compensation',ascending=False)         #Sorting values to get max. compensation count
df_agg =df_agg.groupby('Organization Group').head(1)                      #Selecting each group wise
df_agg
df_agg.to_csv('Q2_P1.csv',columns=['Organization Group','Department','Total Compensation'], index=False, encoding='utf-8')
df_agg.head()


# In[ ]:



