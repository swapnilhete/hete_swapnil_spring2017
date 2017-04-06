
# coding: utf-8

# # Q1_PART_ONE

# In[1]:

import pandas as pd
import datetime as dt
import calendar


# In[2]:

main_data = pd.read_csv('vehicle_collisions.csv',usecols=['DATE','BOROUGH'])    # Getting required data from CSV file

main_data['DATE'] = pd.to_datetime(main_data.DATE)                              #Converting to Date column to datetime64 datatype

st=pd.to_datetime('1/1/2016')                                                  # Defining duration start & end limit 
et=pd.to_datetime('12/31/2016')

conv_data =main_data.loc[(main_data.DATE >=st) & (main_data.DATE <= et)]

conv_data['MONTH'] = conv_data.DATE.dt.month                                  #Adding month column


# In[8]:

temp = []                                     #temp. list to store dataframe

for i in range(1,13):                       # for loop to compute result for 12 months
    count_m = len(conv_data[(conv_data['MONTH']==i) & (conv_data['BOROUGH']=='MANHATTAN')])
    count_t = len(conv_data[(conv_data['MONTH']==i)])
    #print(count_m)
    #print(count_t)
    temp.append({'MONTH': calendar.month_name[i], 'MANHATTAN': count_m, 'NYC':count_t,'PERCENTAGE':((count_m/count_t) )})
final_data = pd.DataFrame(temp)
final_data.to_csv('Q1_P1.csv',columns=['MONTH', 'MANHATTAN', 'NYC','PERCENTAGE'],index=False)
final_data.head()


# In[ ]:



