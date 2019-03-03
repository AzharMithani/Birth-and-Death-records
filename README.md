# Open Data Hackathon - Cleaning and Analysis of Birth and Death records
Data cleaning and analysis of the birth and death records for the Open Data Hackathon organized by PMC Open Data Portal.<br/>
<p align="center">
  <img width="600" height="400" src="https://cdn-az.allevents.in/banners/51cf7ab0-22ce-11e9-b994-439583700c4c-rimg-w526-h388-gmir.jpg">
</p>

Problem Statement: [__opendatapune/birth_and_death_records__](https://github.com/opendatapune/Problem-Statements/wiki/Birth-and-Death-records)
1. Combine various years datasets into a clean machine-readable CSV
2. Derive date-wise, month-wise, year-wise totals by gender and type (birth/death).
3. See monthly trends and year-on-year trends
4. Locate anomalies in the data
5. Compare with historical events, passing of laws like legislation on early sex determination, weather events
6. Compare between the genders
7. Create time series based visualizations, similar to stock market/currency charts.

## Getting Started

### Prerequisites

1. Install and setup Anaconda
Find an easy installation and setup guide using this [link](https://www.datacamp.com/community/tutorials/installing-anaconda-windows)
Make sure you install Anaconda for python 3.6 or above

2. Install the required packages:
Open Anaconda prompt and run these commands
```
conda install pandas, numpy, matplotlib, plotly, psutil, cufflinks, plotly-orca
```
Verify Installation by running
```
import pandas as pd
pd.__version__
```

3. Download the data sets:
<br/>[Dataset for birth_and_death_records](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index?categoryId=50)
<br/>*Optional: Download the whole repository*


### 1. Converting xlsx files to raw csv files

We have taken the input dataset and converted it into pure text CSV format for easy cleaning process.<br/>
"**xlsx_to_csv.p**y" is a script that will automatically convert all the original datasets stored in folder datasets to text CSV format and store them in "**converted/datasets**".<br/>

**Steps to convert the datasets**:
   1. Open Anaconda prompt and go to folder "**opendatapune-birth_and_death_records/converted_datasets**".
   2. Run the commands stored in "**conversion_commands.txt**" for the required conversion.<br/><br/>
Example:
```
python xlsx_to_csv.py ../datasets/"List of Birth And Death rate for the year 2010.xlsx" 2010 birth_and_death_2010.csv
```
<br/>After running all the commands u will see that all the xlsx files are converted to csv files and a essage "Successfully completed" shown after each conversion

### 2. Data Cleaning

The csv files are then cleaned using "**Data_Cleaning_Preparation.ipynb**"<br/><br/>
**Steps in Data Cleaning**:
   1. Corrected miss interpreted dates to dd/mm/yyyy
   2. Split the "Date of Event" and replaced it with "Day", "Month" and "Year"
   3. Used **One-Hot-encoding technique** to store "Type" and "Gender" attributed<br/>
      "**Type**"   -> "Birth" = 0 / "Death" = 1<br/>
      "**Gender**" -> "Male" = 0 / "Female" = 1<br/>
   4. Created Cleaned datasets from year 2010 to 2018 and stored them in folder "converted_datasets"
   5. Combined data from years 2010 to 2018 into single dataset "combined_cleaned_birth_and_death_2010-2018.csv"<br/>

**How to run**:
   1. Open Anaconda prompt
   2. Go to folder "opendatapune-birth_and_death_records"
   3. Type following command to open jupyter notebook
      ```
      jupyter notebook
      ```
   4. Open "**Data_Cleaning_Preparation.ipnyb**" and run each row one by one to clean 

### 3. Data Preparation

Processed the combined raw dataset to get the following information:
1. **Day-wise** data of number of male,female and total births and deaths
   - *Attributes*: Day,Month,Year,male_births,female_births,total_births,male_deaths,female_deaths,total_deaths
   - Stored in file "*Day_wise_information.csv*" in folder "Insights"
   
2. **Month-wise** data of number of male, female and total births and deaths
   - *Attributes*: Month,Year,male_births,female_births,total_births,male_deaths,female_deaths,total_deaths
   - Stored in file "*Month_wise_information.csv*" in folder "Insights"
   
3. **Year-wise** data of number of male,female and total births and deaths
   - *Attributes*: Year,male_births,female_births,total_births,male_deaths,female_deaths,total_deaths
   - Stored in file "*Year_wise_information.csv*" in folder "Insights"
   
4. Male, female and total **Population Growth** per year for 
   - *Atributes*: Year,male_births,female_births,total_births,male_deaths,female_deaths,total_deaths
   - Stored in file "*Recording_differences_between_datasets.csv*" in folder "Insights"<br/>
   
**How to run**
- "**Data_Cleaning_Preparation.ipnyb**" itself does the Data Preparation part.

### 4. Data Visualization
* Note: Clicking on the plot name takes you to the chart which is hosted online on plotly.*<br/>

Visualized the information, extracted from the data, through the following plots:
1. [Daily Birth and Death Trend](https://plot.ly/~gundla.sushant/101)
2. [Monthly Birth and Death Trend](https://plot.ly/~gundla.sushant/103)
3. [Yearly Birth and Death Trend](https://plot.ly/~gundla.sushant/105)
4. [Trend for Male Births](https://plot.ly/~gundla.sushant/107)
5. [Trend for Female Births](https://plot.ly/~gundla.sushant/109)
6. [Trend for Total Births](https://plot.ly/~gundla.sushant/111)
7. [Trend for Male Deaths](https://plot.ly/~gundla.sushant/113)
8. [Trend for Female Deaths](https://plot.ly/~gundla.sushant/115)
9. [Trend for Total Deaths](https://plot.ly/~gundla.sushant/117)
10. [Yearly population growth](https://plot.ly/~gundla.sushant/119)
11. [Yearly Increase/Decrease in Birth Rate](https://plot.ly/~gundla.sushant/121)
12. [Average per Month](https://plot.ly/~gundla.sushant/123)
13. [Swine-flu vs road accidents deaths](https://plot.ly/~gundla.sushant/125)
14. [Seasonal Decompositional analysis for Birth Trend](https://plot.ly/~gundla.sushant/127)
15. [Seasonal Decompositional analysis for Death Trend](https://plot.ly/~gundla.sushant/129)
16. [Future Birth Prediction](https://plot.ly/~gundla.sushant/133)
<br/>

**How to run**:
- Open Plots "**Data_Visualization.ipynb**" and run all code blocks

**Where to find plots**:
   - Plots can be visualized in the "**Data_Visualization.ipynb**" file
   - Plots are stored in "**plots**" folder in image format as well as HTML format.
   - Plots can be viewed online through the links provided next to the plot names.
   
Note: Make use of these **interactive features** of plots for Visualization.
   - Legend(top right) can be used to show or hide a particular trace/bar on the map.
   - Buttons(top left) can be used to select a predefined configuration of traces/bars.
   - Hovering over the plot shows the values corresponding to the x-axis for all traces/bars.
   - Range slider(below x-axis) can be used to choose the range to display on the plot.
   - Pinch to zoom in/out option is available
   
### 5. Analysis and Insights

1. Insights on Daily information<br/>
   - Stored in file "**Daily_Insights.csv**" in folder "Insights"<br/><br/>
   ![Daily_Insights](https://user-images.githubusercontent.com/39993298/52897921-03664900-31fe-11e9-983d-00149f293d7e.png)<br/><br/>
2. Insights on Montly information<br/>
   - Stored in file "**Monthly_Insights.csv**" in folder "Insights"<br/><br/>
   ![Monthly_Insights 23](https://user-images.githubusercontent.com/39993298/52897922-0a8d5700-31fe-11e9-906a-58dadae928f2.png)<br/><br/>
3. Birth and Death Records not registered in "Detected cases and deaths due to diseases" dataset<br/>
   - After comparing our data with the data provided in "Detected cases and deaths due to diseases" dataset available at [link](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index) we found that the later dataset missed many birth and death records<br/>
   - The below table shows the number of birth and death records missing in the later dataset.
.  - Stored in file "**Recording_differences_between_datasets.csv**" in folder "Insights"<br/><br/>
   ![Recording_differences_between_datasets](https://user-images.githubusercontent.com/39993298/52897925-0e20de00-31fe-11e9-9cb5-1d8122a6b17b.png)<br/><br/>

**How to run**:
- Open **"Analysis_and_Insights.ipynb**" file and run all code cells.

### 6. Future Forecasting

We used the monthly data from the year 2010 to 2018 to predict the number of births in the year 2019.<br/>
ARIMA model is used for future prediction which is a state-of-art algorithm in Time-Series Forecasting.<br/>

**How to run**:
- Open "**Forecasting.ipynb**" and run all the code cells
- The results can be seen in the file "**Future Birth Prediction.jpeg**" or "**2019_births_prediction.html**" saved in "plots" folder.

## What does the study tell us

### 1. Important Insights
   - A drastic drop in recorded Birth records was seen in year **2014**. Our insights show a strong correlation with the implementation of the **Two-child policy** in Maharashtra, in the year 2014.
   - In Maharashtra, Pune has the second highest Road fatalities. Our Analysis shows **Road accidents** cause **1.64%** of total deaths in Pune, compared to *0.18%* of that of deadly **swine-flu**.
   - **October** shows **Highest Average Total Births** of *2643* followed by **April** with *2508*. Data shows strong relation with the fact that, in Maharashtra, most of the **marriages* happen in the month of *January* and *September*.
   - Comparing the data found in "**Detected cases and deaths due to diseases**" dataset(available on PMC Open Data Store) and our datasets shows **dramatic differences in the number of birth and death records**. The exact difference in a number of recorded births and deaths from 2 datasets can be seen in file "**Recording_differences_between_datasets.csv**". 
   - **Future Forecasting** predicts the *Number of Total Births* in year **2019** will be **48,824**
   
### 2. Anomalies in data

   - The number of Birth records on **28 and 29 Apr 2018** were **suspiciously low** than mean (average) daily births.
   - The number of Death records between **30 Jun to 30 Jul 2017** were **suspiciously low**. News shows no evidence of hospital shutdowns or strikes.
   - Prior half of **Aug 2016** shows high number deaths indicating some kind of **epidemic**, but analysis of news from July and Aug 2016 shows no evidence of an epidemic in Pune city. The reason for such high death records is not yet clear.
   - **Oct 2013** recorded highest births of *5640* in any month in past decade. The data looks anomalous, but after comparing the data to the "Detected cases and deaths due to diseases" dataset, it was found that the recorded data was true.
   - The number of Birth records in year **2010** were lowest indicating poor birth data recording that year.
   - Year **2016** recorded the highest number of deaths *31,374* in any year. The year 2016 is the only year that does not follow the normal trend in death records of *25k-30k*.
   
### 3. Insights from the data
   - **Highest #Birth records** of *298* was recorded on **10 Nov, 2011**, in past decade.
   - **Female to Male Population growth** was **123.5%** shows increase in female population than male population in Pune.
   - **Female to Male Birth Ratio** was **92.2%** indicating almost same male vs female births.
   - **Female to Male Death Ratio** was **69.73%** indicating lot more male deaths than female deaths.
   - **Highest population growth** of *30,928* was recorded in year **2013** and **Lowest population growth** of *24,255* was recorded in year **2016**.
   - **Aug 2016** recorded highest deaths of *3217* in any month in past decade.
   - **Jul 2017** recorded lowest deaths of *1177* in any month in past decade.
   - Drastic **Decrease in Birth Rate** was seen in years **2014 (-14.25%)** and **2016 (-8.18%)** from espective previous years.
   
   
## Conclusion
 
 - In Maharashtra state, **Pune** city has **Highest Road Fatalities** after Mumbai City. Every year, over 400 people lose their lives in road accidents. Stats show that only **16 of every 100 people** are seen wearing helmets in Pune. While Departments of **Insect Control** and **Epidemic Disease Control** of **Pune Municipal Corporation** are doing a good job to keep the **Deaths caused due to diseases** as low as **0.2%** of total deaths, Pune **road fatalities** cause more than **1.6%** deaths of all deaths.<br/>
- Pune Road safety authorities must do something to bring down the road fatalities to decrease the deaths in Pune city.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Azhar Mithani** - [LinkedIn Profile](https://in.linkedin.com/in/azhar-mithani)

<!---
## License 
his project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
-->

## Acknowledgments

* Pune Open Data portal for providing with data

## Resources

- https://www.hindustantimes.com/pune-news/why-are-we-driving-ourselves-to-death-are-the-roads-in-pune-safe/story-xr4ZCTYgiBp0TXD5Krc20M.html
- https://timesofindia.indiatimes.com/city/pune/referral-cases-raise-swine-flu-death-count-in-state/articleshow/67315778.cms
