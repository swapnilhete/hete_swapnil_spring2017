
# coding: utf-8

# # Q3_PART_ONE

# In[1]:

import pandas as pd


# In[17]:

# Get required columns from dataset
main_data = pd.read_csv('cricket_matches.csv',usecols=['home','winner','innings1','innings1_runs','innings2','innings2_runs'])


#Obtain new dataframe based on winner and innings 
main_data_in1=main_data[(main_data['winner']==main_data['innings1'])]
main_data_in2=main_data[(main_data['winner']==main_data['innings2'])]


#Create new dataframes wrt above step and obtain respective innings run
df1 = pd.DataFrame({'home': main_data_in1['winner'], 'Runs': main_data_in1['innings1_runs']})
df2 = pd.DataFrame({'home': main_data_in2['winner'], 'Runs': main_data_in2['innings1_runs']})

#Merge inning1 and inning2 data to calculate aggregate
result = df1.append(df2, ignore_index=True)
result = result.groupby(result['home']).mean()
result=result.reset_index()
result.head()



# In[18]:

result.to_csv('Q3_P1.csv',index=False, encoding='utf-8')        # Saving datafram to csv


# In[ ]:



