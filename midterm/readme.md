
# Midterm Question 1

**Analysis 1 - Sent Email Analysis from 10-1998 to 07-2002**                                                                     

File Name : Midterm_Q1_Analysis1

Location  : \midterm\Question 1\Analysis 1

Input Data : \midterm\data\enron\*

Output Data : A graph and CSV file \midterm\Question 1\Analysis 1\sentItem.csv


Solution:
    1. Data is extracted to input folder
    2. All required lib. are imported
    3. 'sent_item_details' this dictionary is initialized to store all required data
    4. sentFunction() will parse each email and get msg ID and date for respective email. Date is converted into required format
       and then data is stored dictionary initialized in step 3
    5. Next block iterate through each type of sent file folders for each user. Enron data set has 3 types of sent folder
       sent / _sent_mail / sent_items
    6. Function declared in step 4 is called each time to get result. A print statement is added to keep track of program
       progress
    7. sent_year_count dictionary will maintain count of emails against each month-year combination for further processing
    8. A graph of month-year on x-axis vs count on y-axis is plotted with matplotlib. rcParams package is imported for      
    displaying and formating generated graph. A lamba function is used on dictionary to sort it date wise
    9. Data is stored in csv file  for additional referecne
 
    

![Analysis 1](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q1A1.JPG)

**Conclusion** - As per the graph the volume of sent items are increased 12/1999 till 05/2001 this signify that there is lot of discussion going on between enron employee and this duration also corresponds to the year when scandal was busted. This duration can be used to analyse email more for further investigation

**Analysis 2 - Top 25 email sender users by sent item and total emails**                                                                     

File Name : Midterm_Q1_Analysis2

Location  : \midterm\Question 1\Analysis 2

Input Data : \midterm\data\enron\*

Output Data : A graph and CSV file \midterm\Question 1\Analysis 2\userCount.csv

1. All required lib. are imported
2. Lists are declared to store data. 4 fucntions are defined userName() - to extract user , inboxCount() - Count no. of emails in inbox for each user, sentCount() to count no. sent items from all folders, deleteCount() count no. of deleted items
3. A csv 'usersCount' is genrated to store count for each user for reference
4. A lambda function is used to sort and get top users from each type i.e inbox,sent,deleted
5. Two temp dictionaries are created for storing graph data
6. Two graphs are plotted for top 25 users who sent max. emails and another graph was plotted for top 25 users who has max. no. of emails in their folder

![Analysis2A](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q1A2a.JPG)
![Analysis2B](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q1A2b.JPG)

**Conclusion** - In this analysis out of 151 users 25 users are shortlisted based on their email activities which might be responsible for fruad activities. This list has almost all top names which found to be accussed in Enron scandal 

**Analysis 3 - Sentiment analysis of fraud words on top sudpected users**

File Name : Midterm_Q1_Analysis3

Location : \midterm\Question 1\Analysis 3

Input Data : \midterm\data\enron\* , \midterm\data\enron_created, \midterm\output\badwords.txt

Output Data : A pie chart and txt file \midterm\output\suspectedUsers.txt

Solution:
   1. All requred lib. and NLTK corpus is imported
   2. A list of top suspected users from last analysis is fetched ans stored in suspectedUser list.
      Also a list of bad words which are related to fraud are computed manually from complete data set and word count. This list 
      will be reference for each uses own word list to count sentiment analysis index of fraud words
   3. A txt file corresponding to each user is created in location midterm\data\enron_created this folder has txt file of each    
      user and his sent item email conversation in form of words
   4. All these generated files are reference to calculate sentiment index. Various list are initialized in this step
      user_word_clean - clean words from sent items, std_words this list consist of standard word spoken in English lang.
      user_word_required - this list is combination of words found in each user sent item and which are standard. Thus
      eliminating unwanted words. 
   5. final_frequency dictionary is maitained to store each user and his sentiment count to plot a graph
      Note: Here I have considered only top 4 user for analysis reason being sent word list for each user was huge and txt file      created was of size 7+ MB. System was taking more time (7-8 hrs) to process those and hence I have considered only top 4 
      users but same logic can be implemented for each user to get sentiment.
    6. A pie chart of each user is plotted with sentiment count. Each bad word is allocated count of 1 and summation of all word
       bad count gives fraud sentiment for that user. Fraud word includes such as money,call,meeting,discuss and other stock and        share market related terms.
 
 
 **Conclusion** - From pie chart it is clear that user such as Skilling,Lay and scott are having higher fraud sentiment index. Which indicates that these person might be higly involved in Enron scandal. Same sort analysis can be implemented for each user. This might help in further investigation of selected users out of 150 users
 ![Analysis3](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q1A3.JPG)

# Question 2

**Analysis 1 - NYT year wise food artical distribution and  food section statistics**                                                                     

File Name : Midterm_Q2_Analysis1

Location  : \midterm\Question 2\Analysis 1

Input Data : \midterm\data\food\*

Output Data : A graph and CSV file midterm\\data\\output\\foodDetails.csv


1. Required lib are imported
2. Artical search, Archieved and Most popular APIs are used to download data related to food. This data consisted of articals from 1990 to 2015 and required page offset is used to fetch data. There are limitation of 120 pages to fetch data hence around 2.90MB data I was able to download for this category
3. Data is stored in /midterm/data/food section. Required url is constructed to get all data year wise and page wise
4. All data then stored in json file for easy navigation
5. From each food artical unique data is fetched and stored into list it consist of articalID,published data and section which are most useful
6. Also data is stored into CSV for easy reference. (midterm\data\output\foodDetails.csv)
7. A count of artical published against each year is obtained and plotted
8. Also artical according to sections are formed. This data is stored in pie chart

**Conclusion** - From the first graph it is observed that most no. of articals are published for duration of 1995-2000. These artical mostly involved cooking recipes. Due to increased in no. of restaurent in intial year of 21st century there might be decline in food-recipes related articals and most of articals was ralted to dinning outside in hotel and restaurents.

A pie chart shows most of artical contribution was through NYT magazines and 2nd most favorite artical section was Dinning and wine for outside activities.
![Analysis1A](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q2A1a.JPG)
![Analysis2A](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q2A1b.JPG)

**Analysis 2 - Top 15 IT companies discussed based on NYT artical **                                                                     

File Name : Midterm_Q2_Analysis2

Location  : \midterm\Question 2\Analysis 2

Input Data : \midterm\data\technology\*

Output Data : A graph and CSV file midterm\\data\\output\\technologyDetails.csv

Solution:
 1. Reuqired lib are imported
 2. Artical search, Archieved and Most popular APIs are used to download data related to technology. This data consisted of articals from 1990 to 2015 and required page offset is used to fetch data. There are limitation of 120 pages to fetch data hence around 2.65MB data I was able to download for this category
 3. Data is stored in /midterm/data/technology section. Required url is constructed to get all data year wise and page wise
 4.All data then stored in json file for easy navigation
 5. From each technology artical unique data is fetched and stored into list it consist of articalID,published data and section   which are most useful
 6. Also data is stored in CSV for easy reference.( midterm\data\output\technologyDetails.csv)
 7. Each artical snippet is analysed and word count againt each company with companylist.txt file is calculated. Based on top grossing and artical related to companies count is derived.
 8. Later data is stored in bar chart using matplotlib
 
**Conclusion** - As most of data was from 90's there was boom for Microsoft products especially windows Pc and windows 98 and XP system. Hence Microsoft is at top position for all articals followed by IBM for its enterprise related software in demand during late 19 century.
![Analysis2](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q2A2.JPG)

**Analysis 3 - Top popular countries in tourism from NYT travel articals **                                                                     

File Name : Midterm_Q2_Analysis3

Location  : \midterm\Question 3\Analysis 3

Input Data : \midterm\data\travel\*  & midterm\\data\\travel\\country.txt

Output Data : A  bar graph and CSV file midterm\\data\\travel\\travelDetails.csv

Solution:
 1. Reuqired lib are imported
 2. Artical search, Archieved and Most popular APIs are used to download data related to travel. This data consisted of articals from 1990 to 2015 and required page offset is used to fetch data. There are limitation of 120 pages to fetch data hence around 2.92 MB data I was able to download for this category
 3. Data is stored in /midterm/data/travel section. Required url is constructed to get all data year wise and page wise
 4.All data then stored in json file for easy navigation
 5. From each travel artical unique data is fetched and stored into list it consist of articalID,published data and section   which are most useful
 6. Also data is stored in CSV for easy reference.( midterm\\data\\travel\\travelDetails.csv)
 8. Each artical snippet is analyzed and extracted. Artical content is checked against list of country and corresponding country and artical published year is maintained in a list. 
 9. A separte year list when articals are published is maintained in year_list
 10. Based on country and its artical published in that year. Unique count is maintained in dictionary
 11. A bar graph with countries 79 and its popularity index is plotted
 
 **Conclusion** - From the bar graph its is clear that advance countries where living standard of person is higher has most popularity in terms of tourism and travel. Companies with vibrant culture and largest  scenic land area are scoring top point in this analysis. This analysis includes top contries from respective continent. 

![Analysis3](https://github.com/swapnilhete/hete_swapnil_spring2017/blob/master/midterm/output/Q2A3.JPG)

```python

```
