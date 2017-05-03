
# Dataset

This dataset contains information about Airline on-time performance in the USA on the domestic flight. I have used data for the year 2015-2016 for analysis. The data is created and maintained by United States Department of Transportation. 

This data can be found and downloaded with below link:

Beuro of Transportation Statistics:

https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time

Folder Structure : 
1. \Data\Carriers\L_UNIQUE_CARRIERS.csv - Contains details about  carrier code and their description - Used as lookup file

2. \Data\Location_Data\us_postal_codes.csv  - Contains details about city,latitude,longitude - Used as lookup file
3. \Data\Main_Data - Contains CSV file for year 2015-16. This folder has only sample data(256MB). Actual data can be downloaded
   from original site or from google drive link (refer readme.txt)
4. \Data\Rating_Data - Contains airport rating provided by the user. used as lookup file

Metadata:
Below is column structure of each CSV file:
![Metadata](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/Metadata.png)



# Analysis 1 - Analysis on Airports 

File Name : Final_1.ipynb

Location  : \Final\Analysis\

Input Data : \Data\Main_Data\* and \Data\Rating_Data\airport.csv

Output Data :  \Output\Final_Analysis_1\*


This analysis provides information about various airports and its traffic in the USA. 


**PART A**

From original dataset columns such as YEAR, ORIGIN(source airport), DEST(Destination airport) details are fetched.  A group by the function is applied to DEST and ORIGIN airport code separately and a count is calculated. Two data frame are then appended to final list of count on each airport w.r.t. incoming and outgoing traffic. The final data frame output is stored into file A1_Top_20_Airports.csv. This file contains all airports and no. of flights operated during 2015-2016.

A horizontal bar graph of Airport v/s No. of flights is plotted.
It is found that ATL(Atlanta) airport served maximum no. of flights (1.5M) during these two years followed by Chicago(ORD) and Dallas(DFW). Top 10 spot is occupied by that airport which is present in most of the metro city. The distribution is concentrated in areas where the population is more. Ex. On northeastern region, Newyork and Boston served most of the flight while on west coast region California cities served most no. of flight. Texas airport is the leader in the middle part of USA. Also, these top 10 airports serve most of the traffic because they are also connected with international airport destinations.

![A1_Top20_Airport](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A1_Top20_Airport.png)


**PART B**

From the original dataset columns such as airport_name,overall_rating, queuing rating,terminal_cleaniness, shopping are extracted and stored in the data frame. All this data is then grouped by Airport name. For making analysis limited below airports are selected which were the busiest airport in part A analysis - ATL, DFW, LAX,  ORD, SFO. There were certain entries where particular users have not submitted any rating so those NaN values are replaced with 0. Average function is applied on each numeric column of a dataframe to get Avg rating at each airport.

A use of grouped bar chart shows that ATL and SFO are the highest achievers of rating in all terms 0- being poor to 5 being excellent.  SFO and ATL airport scored overall rating of above 4 while rest of airports are below Avg. rating i.e. 3. All airport has very poor queue rating beause these airport belongs to busiest catergory and hence there is always rush of people leading to more security and checking time .This statistic can help airport authorities to improve passenger services in particular area where the rating is low.

![A1_Top5_Airport_Ratings](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A1_Top5_Airport_Ratings.png)

**PART C**

This part covers analysis on the amount of traffic increased/decreased from the year 2015 to 2016. From original dataset fields such as year, origin and destination are extracted.  Based on these field count for inbound and outbound traffic is computed for each year. A final data frame is constructed by joining 2015 and 2016 data for total no. of flights. A deviation in terms of percentage is derived for each airport. A top 10 and bottom airport which shows increase and decline in no. of flights is populated. Details air traffic deviation at each airport is stored in CSV file A1_Airport_Traffic_Deviation.csv.  That airport which showed decline are highlighted in red and with an increase in traffic are highlighted with green. 

A tabular result shows that traffic at major airport remains same throughout year 2015 and 2016. The change was reported are list famous airport such as Tompkins Cty, Bangor International, Springfield-Branson Regional etc which was developed recently by USA government.

![A1_Top10_Aiport_Traffic_Deviation2016](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A1_Top10_Aiport_Traffic_Deviation2016.png)


# Analysis 2 - Analysis on Flight Routes 

File Name : Final_2.ipynb

Location  : \Final\Analysis\

Input Data : \Data\Main_Data\* and \Data\Location_Data\us_postal_codes.csv

Output Data :  \Output\Final_Analysis_2\*


**PART A**


This part of analysis covers all flights routes in the year 2015-2016. From original dataset fields such as origin source city and destination city name is extracted. Then a unique combination of each source to destination is formed by grouping these two columns. A count of each unique route is taken.  From different data, CSV file details about location and its latitude and longitude are extracted. Inner join on two data frame is performed to get the city and its corresponding latitude and longitude in order to plot in on USA map.All duplicated entries are dropped. Since original lat. and long. are in object form they must be converted into a numeric format.  A route density is stored in A2_Routes_density.csv.  Use of plotly library and scatterplot to map lines between source and destination. Also, a  list of airports from source and destination is constructed to plot as a dot in USA maps. 

Major traffic routes are situated on the west coast and east coast region. There is airlines hub like San-Fransico , Atlanta, Chicago. Where maximum no. of flights are originating and departing.  As per the map, most frequent flying routes are SF to NY, Dallas to Boston, Chicago-Atlanta-Miami. Except for Seattle north-western part of USA has very less density of flights. 

![A2_Route_Density](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A2_Route_Density.png)

**PART B**


This analysis covers top 8 routes for the year 2015 and 2016. The purpose of this analysis is to show how frequent flyer routes performed in the year 2015-16. In order to meet this requirement year, source city and destination city are extracted from the original dataset. Count function is applied to this column to get no. of flights and then later it is filtered based on year. A route column is constructed for few cities for further analysis. The details of required data frame are stored in A2_Busy_Routes.csv.

A time series graph is plotted w.r.t two traces i.e. 2015-2016. The amount of traffic is only increased for SFO-LA route for the year 2016. Rest all busy routes showed a decline in traffic. Also from each Source -destination there was the equal amount of return flight for that year. This analysis shows that airlines face maximum competition on these routes. Except west coast route (SFO_LA)all north-east route(NY-CHI,BOS-NY,NY_LA) shows declined in traffic for year 2016.

![A2_Busy_Routes](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A2_Busy_Routes.png)

**PART C**

This analysis is carried out in order to determine best travel time to particular cities where there is two airports. This study shows that user can opt for the particular airport to save his journey time. Two cities Chicago and New york are selected for this analysis. These cities have multiple airports. Month, actual_elasped_time, source and destination columns are selected for this analysis. Few common routes such as NY-BOS, CHI-BOS, CHI-NY are selected. A month wise count is taken by grouping these cities. Corresponding to each source-destination different data frame are formed and fed as input to the graph.

The analysis shows that if flyer wants to travel to NY he should opt for LGA airport which has Avg. 10 min of less duration compares to JFK airport. Also, JFK airport has more traffic compare to LGA.  May - Aug is duration, where there is always more flight duration, compare two other months of a year for flyer landing in NY. Similarly for Chicago MDW is the best airport to travel from any city as it has less travel duration compare to ORD airport which is combination International and Domestic flight airport

![A2_Newyork](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A2_Newyork.png)

![A2_Chicago](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A2_Chicago.png)

# Analysis 3 - Analysis on Airlines and its performance

File Name : Final_3.ipynb

Location  : \Final\Analysis\

Input Data : \Data\Main_Data\* and \Data\Carriers\L_UNIQUE_CARRIERS.csv

Output Data :  \Output\Final_Analysis_3\*


**PART A **

Below analysis get top most airlines based on no. of flight services they serves in the USA Selected columns such as carrier, canceled, delayed and diverted flight with their reasons. Another CSV file L_UNIQUE_CARRIERS.csv is used to get airline code and its description. An inner join is performed on these two data frames to get complete carrier name.  A count function is used to get no. of flights operated by these airlines for the year 2015-16. The final data frame result is stored in A3_Top_Carriers.csv for reference.

Using plotly a vertical bar graph is plotted. With Airlines with max. no. of services are on left-hand side of a graph with airlines which low services are on the right-hand side of the graph. Airlines such as Southwest, Delta, American Airlines are the leader in USA domestic services. Southwest airlines served almost 2.5 M flight in these two years.

![A3_Top_Airlines](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A3_Top_Airlines.png)

** PART B**

This analysis correspondence to airlines and its performance on factor like no. of flights canceled, delayed and diverted. There are various factors which result in suspension of flights. Below graph will highlight those and check what are the reason and major contribution for same. Three data frame are created for each performance factor. All these data frames are then joined with carrier data frame to form the final data frame. Percentage of each category is calculated based on total no. of flights. The required result is stored in A3_Airline_performance.CSV file.

A stacked bar chart is very useful in this analysis. It shows airlines with worst performance on these 3 factors and their individual ration. Even though Southwest servers most no. of flights, their performance is much better than other airlines hence they are a top most choice for customers for reliability. Hawaiian Airlines has worst performed in all airlines. Out of all these performance factors delay is the most common reason and next analysis will show various reason behind it. 

![A3_Airline_performance](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A3_Airline_performance.png)


# Analysis 4 - Analysis on Airlines and its performance

File Name : Final_4.ipynb

Location  : \Final\Analysis\

Input Data : \Data\Main_Data\*

Output Data :  \Output\Final_Analysis_4\*

**PART A**

Below analysis will explain Arrival and Departure delays of all airlines and how they have changed from the year 2015 and 2016. In order to perform this analysis columns such as carrier, origin, destination, departure delay and arrival delays are extracted from local data. A mean function is applied to this column to get Avg. the value of arrival and departure delays. These values are stored in python variable for scalar operation on data frame.  Data frame is group by an airport and corresponding delays are calculated. A new data frame is formed by performing joins to get the percentage of delays across an airport. Final output is stored in A4_delay_stat.csv.

For this analysis, a bar chart with subplot is plotted using plotly. The main feature of this chart is it will show both positive and negative Avg value for both delays. Ex. ATL, PHX, SEA are the airport which shows improved performance in terms of delay compared to overall delays occurs in USA.
 
![A4_Arr_dep_sub](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A4_Arr_dep_sub.png)


**PART B**

This analysis will be the continuation of analysis 3 where most of the delays occurred in flight routes are due to arrival and departure delays. This analysis will highlight common cause like canceled flights, weather, security, late aircraft and other(NAS) delays. Year wise data frame is created for each section of delays. Also, the percentage of each category is calculated and plotted as below. A4_delay_donuts.CSV file has all details about these delays.

A donut shape pie chart is used for this analysis. Two pie charts for the year 2015 and 2016 are formed and criteria of delay and its percentage are plotted. NAS and Late aircraft were most responsible for flight delays during both areas. While delayed occurred due to security and weather are not that much significant.

![A4_Delays_Pie](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A4_Delays_Pie.png)


**PART C**

A heat map for Airlines and their respective delays is plotted. This heat map shows that Security delays are at the lowest level for all airlines. While the F9 airline has most no. of delays due to late aircraft.This co-relation data is stored in A4_delay_corelation.csv

![A4_Delays_Heatmap](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A4_Delays_Heatmap.png)


# Analysis 5 - Geographic and Month wise Analysis

File Name : Final_5.ipynb

Location  : \Final\Analysis\

Input Data : \Data\Main_Data\*

Output Data :  \Output\Final_Analysis_5\*

**PART A**

This analysis covers state wise distribution of no. of flights operated by all airlines. The USA heat map is formed showing the density of flights for the year 2015-2016. Carrier, a state of origin and flight no. are the details extracted from original data. Sum of flight by an airline is performed on Flight no. column. A state-wise data is stored in CSV A5_State_data file.

choropleth type of plotly graph is used in this analysis. It will highlit states on basis of no. the flight operated with the color gradient. From this graph, it is very easy to understand region where most no. of air traffic data is. California and Texas are the top most areas having 1.4 M and 1.2 M of a fight scheduled for these two years. North most region has very low flights due to its scarcity in population.

![A5_State_heatmap](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A5_State_heatmap.png)

**PART B**

Below analysis is performed on month wise data for all flights to figure out maximum possible chances of delays occurs for airlines. 
This time plot has input based on year, month, departure and arrival delay timelines. Flight count is calculated grouping month and year of extracted dataset. As per the time slot graph, maximum delays occurs during holiday period i.e in summer and in December. This analysis will help airlines and airport authority to prepare well in advance to minimize human reported delays well in advance.

![A5_Delayed_timeSeries](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/A5_Delayed_timeSeries.png)


# Special Instruction

** Viewing .ipynb files**

Since I have used plotly. Graphs will not be visible in Github link. Please use below link of nbviewer to view code with graphs

http://nbviewer.jupyter.org/github/swapnilhete/hete_swapnil_spring2017/tree/master/Final/Analysis/

** Dataset Instruction **
I was not able to upload full data set(2.5GB). Hence sample data is uploaded. Please download dataset with google drive link provided in readme.txt file in data folder

Download data from original source will look like this:
![data](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/data.png)


**Addtional library import **
Please import below plotly and cufflink library(offline Mode). Attached are screenshorts and command
conda install plotly

![plotly](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/plotly.png)

pip install cufflinks

![Cufflink](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/Cufflink.png)

pip install cufflinks --upgrade
CuffLink2

![CuffLink2](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/Final/Images/CuffLink2.png)






```python

```
