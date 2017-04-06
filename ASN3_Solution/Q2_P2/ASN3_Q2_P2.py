
# coding: utf-8

# # Q2_PART_2

# In[20]:

import pandas as pd
import datetime as dt
import calendar


# In[21]:

main_data = pd.read_csv('employee_compensation.csv')    # Reading CSV file
#main_data.head()


# In[22]:

calendar_data = main_data.loc[main_data['Year Type'] == 'Calendar']  # Getting only calendar data 
#calendar_data.head()


# In[23]:

required_data = calendar_data[['Job Family','Employee Identifier','Salaries','Overtime','Other Salaries','Total Salary','Retirement','Health/Dental','Other Benefits','Total Benefits','Total Compensation']]
avg_data = required_data.groupby(['Employee Identifier','Job Family']).mean()
#avg_data.head()                                                               #calculated average on each column


# In[24]:

sal_data = avg_data[avg_data['Overtime'] > 0.05*avg_data['Salaries']]        # Expression for overtime salary > 5% 
sal_data = sal_data.reset_index(drop=False)
req_data = sal_data[['Job Family','Total Benefits','Total Compensation']]


# In[30]:

finaL_result = req_data.groupby(['Job Family']).mean()


# In[32]:

finaL_result['Percent_Total_Benefit'] = finaL_result['Total Compensation'] / finaL_result['Total Benefits']
#finaL_result.to_csv('Q2_P2.csv',index=False, encoding='utf-8')
#added additional column for percent
finaL_result.head()


# In[35]:

final_result = finaL_result.reset_index(drop=False)
finaL_result.to_csv('Q2_P2.csv',index=False, encoding='utf-8')


# In[ ]:



