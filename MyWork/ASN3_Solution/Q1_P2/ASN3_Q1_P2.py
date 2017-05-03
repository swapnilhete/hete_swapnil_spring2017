
# coding: utf-8

# # Q1_PART_TWO

# In[33]:

import pandas as pd
import datetime as dt
import calendar
import numpy as np


# In[35]:

main_data = pd.read_csv('vehicle_collisions.csv',usecols=['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']) 
main_data.head()      # Selecting reequired columns


# In[36]:

#myfunction = lambda x: x.notnull().astype('int')

main_data['V1_Num']=main_data['VEHICLE 1 TYPE'].notnull().astype('int')   # Converting vehicle type columns to 0 & 1
main_data['V2_Num']=main_data['VEHICLE 2 TYPE'].notnull().astype('int')
main_data['V3_Num']=main_data['VEHICLE 3 TYPE'].notnull().astype('int')
main_data['V4_Num']=main_data['VEHICLE 4 TYPE'].notnull().astype('int')
main_data['V5_Num']=main_data['VEHICLE 5 TYPE'].notnull().astype('int')

main_data['sum'] =main_data.sum(axis=1)      # Adding sum column for aggregation of each borough
#main_data
#main_data.to_csv('Q1test.csv',columns=['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE','V1_Num','V2_Num','V3_Num','V4_Num','V5_Num','sum'],index=False)


# In[39]:

br = ['BRONX','QUEENS','BROOKLYN','MANHATTAN','STATEN ISLAND',np.NaN]   # List of all Borough 
result =[]    # List to store results


for b in br:
    count1 = 0                          #Declaring counts to maintain no. of vehicle records
    count2 = 0
    count3 = 0
    countM = 0
    
    
    #Getting count of accidents records for each borough with specific no. of vehicles
    
    count1= len(main_data[((main_data['BOROUGH']==b)| (main_data['BOROUGH']).empty) & (main_data['sum']==1)])
    count2= len(main_data[((main_data['BOROUGH']==b)| (main_data['BOROUGH']).empty) & (main_data['sum']==2)])
    count3= len(main_data[((main_data['BOROUGH']==b)| (main_data['BOROUGH']).empty) & (main_data['sum']==3)])
    countM= len(main_data[((main_data['BOROUGH']==b)| (main_data['BOROUGH']).empty) & (main_data['sum']>3)])
    
    
    #appending result to list
    result.append({'BOROUGH':b, 'ONE_VEHICLE_INVOLVED': count1, 'TWO_VEHICLES_INVOLVED':count2,'THREE_VEHICLES_INVOLVED': count3,'MORE_VEHICLES_INVOLVED': countM})
    
    
#Storing data to dataframe and CSV
final_data = pd.DataFrame(result)
final_data.to_csv('Q1_P2.csv',columns=['BOROUGH', 'ONE_VEHICLE_INVOLVED', 'TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED'],index=False)
final_data.head()
        
            


# In[ ]:



