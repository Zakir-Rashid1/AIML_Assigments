
#Artificial Intelligence and Data Science
#Assignment 03

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Problem A:  Data Extravaganza – Unleash the Visual Delight!

#A_1: The Prelude: Navigating the Data Odyssey

#Load the dataset into pandas dataframe
product_price_df = pd.read_csv("./Data_Sets/Product_price_index/ProductPriceIndex.csv", index_col=0)

#Revealing the structure of data
print(f"Shape of dataset: {product_price_df.shape}")

#Introducing the dataset with the first few rows
product_price_df.head()

#Rename column names to some meaningful column names
new_col_names = {
    "farmprice": "farm_price",
    "atlantaretail" : "atlanta_retail",
    "chicagoretail": "chicago_retail",
    "losangelesretail": "losangeles_retail",
    "newyorkretail": "newyork_retail",
    "averagespread": "average_spread"
}
product_price_df = product_price_df.rename(columns=new_col_names)


#Function that'll convert object dtypes into str and flaot dtypes respectivelly
def convert_dtypes():
    #Convert productname into str object
    product_price_df.index = product_price_df.index.astype(str)

    #Convert rest object into float
    #Iterate over column names of dataset
    for col_name in product_price_df.columns[1:6]:
        #Replace $ with empty string, and then replace empty string with np.nan
        product_price_df[col_name] = product_price_df[col_name].str.replace("$", "").replace("", np.nan)
        #Now convert the string into float dtypes
        product_price_df[col_name] = product_price_df[col_name].astype(float)

    #Convert dtype of last col into float
    product_price_df["average_spread"] = product_price_df["average_spread"].str.replace("%", "").str.replace(",", "").replace("", np.nan)
    product_price_df["average_spread"] = product_price_df["average_spread"].astype(float)
    
    

convert_dtypes()









#A_2: The Data Exploration: Unlocking Insights

#Decode data types of each columns
print(f"Data types of each feature:\n{product_price_df.dtypes}")

#Begin a statistical journey
print("Complete statistical analysis of my dataset is:")
product_price_df.describe()






#A_3: The Visual Techniques: Beyond the Basics
product_price_df.head()

#Explorining the relationship between 'productname' and 'farm_price' and 'atlanta_retail'
#Create a figure of size (10, 6)
plt.figure(figsize=(10, 6))



#Overview of data by scatter plot
plt.scatter(product_price_df['farm_price'], product_price_df['atlanta_retail'], color="hotpink", 
            label="Farmer Price Vs Atlanta Retail Price")
plt.scatter(product_price_df['farm_price'], product_price_df['chicago_retail'], color="green",
            alpha=0.4, label="Farmer Price Vs Chicago Retail Price")
plt.scatter(product_price_df['farm_price'], product_price_df['losangeles_retail'], color="blue", 
            alpha=0.1, marker=".", label="Farmer Price Vs Losanagle Retail Price")


plt.title("Graphical Visualization of Data")
plt.legend()
plt.show()




#Raise the curtain with a Bar Plot—highlight two or more quantities of your choice
#Bar plot b/w product name vs (farmar price, atlant retail price and chicago retail price

#Select product names
product_names = product_price_df.index
#Group them by product names and find mean in each case
avg_buy_sell_price = product_price_df.groupby([product_names])[["farm_price", "atlanta_retail", "chicago_retail"]].mean()

#Get unique product names
unique_product_names = product_price_df.index.unique()
equal_intervals = np.arange(len(unique_product_names))

#Set width and multiplier
set_width = 0.25
multipiler = 0

fig, ax = plt.subplots(layout='constrained', figsize=(12, 6))

#Plot different bar graphs
for col in avg_buy_sell_price.columns:
    ax.bar(equal_intervals + set_width * multipiler, avg_buy_sell_price[col], width=set_width, label=col)
    multipiler += 1


ax.set_xlabel("Product Names")
ax.set_ylabel("Price in USD")
ax.set_title('Product Vs Price')
ax.set_xticks(equal_intervals + set_width, unique_product_names)
ax.legend(loc='upper left', ncols=3)
plt.xticks(rotation=45)
plt.show()



#Illuminate correlations with a Color Plot (Heatmap)
#Plotting the corelation b/w product name and retial price in atlantica
correlation_matrix = product_price_df.iloc[:, 1:].corr()
print(f"Co-relation matrix:\n")
correlation_matrix


import seaborn as sns #Used only to draw heatmaps with ease
#Plotting corealtion matrix using heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()


#Craft a Histogram—observe the distribution of different variables.
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

#Plotting fist historgram of farm price
axs[0, 0].hist(product_price_df["farm_price"], bins=50, color='skyblue', edgecolor='red')
axs[0, 0].set_xlabel('Farm Selling Price In USD')
axs[0, 0].set_ylabel('Frequency of Selling Products')
axs[0, 0].grid(True)

#Plotting second historgram of atlanta retail price
axs[0, 1].hist(product_price_df["atlanta_retail"], bins=50, color='orange', edgecolor='red')
axs[0, 1].set_xlabel('Atlanta Retail Price In USD')
axs[0, 1].set_ylabel('Frequency of Selling Products')
axs[0, 1].grid(True)

#Plotting third historgram of chicago retail price
axs[1, 0].hist(product_price_df["chicago_retail"], bins=50, color='cyan', edgecolor='red')
axs[1, 0].set_xlabel('Chicago Retail Price In USD')
axs[1, 0].set_ylabel('Frequency of Selling Products')
axs[1, 0].grid(True)


#Plotting four historgram of losangeles retail price
axs[1, 1].hist(product_price_df["losangeles_retail"], bins=50, color='skyblue', edgecolor='red')
axs[1, 1].set_xlabel('Losangeles Retail Price In USD')
axs[1, 1].set_ylabel('Frequency of Selling Products')
axs[1, 1].grid(True)

fig.suptitle('Histograms of Various Prices', fontsize=12)
plt.show()



#Serve insights with a Pie Chart—visualize different contributions.
#Find avg. spread group wise
avg_spread_group_wise = product_price_df.groupby(["productname"])["average_spread"].mean()
_labels = product_price_df.index.unique()
plt.figure(figsize=(8, 8))
plt.pie(avg_spread_group_wise, labels=_labels, shadow=True)
plt.title("Avg. Distribution of Vegetables Group Wise")
plt.show()






"""
 A_4: The Evaluation: Which Graph Stole the Spotlight?
-Scatter Plot: The scatter plot provides me with a rough idea of how the data is distributed across the range of values. It visualizes the relationship between the variables and helps me identify any patterns or trends. However, despite its usefulness in giving an overview, the distribution plot, which provides more detailed information about how the data is spread out, did not offer much assistance in this particular context. It may be that the distribution plot lacked clarity or did not reveal any additional insights beyond what was already apparent from the scatter plot.
-Bar Plot: The bar plot helps me understand the price differences of products sold in various parts of the cities. It provides a comprehensive overview of the cost variations, indicating whether the products are being sold at higher or lower prices. This visualization offers valuable insights into the profitability for retailers, illustrating how much profit they make after purchasing products in smaller quantities from farmers. By comparing prices across different areas, I can assess market trends and make informed decisions about purchasing and selling strategies
-Heat Map: The heat map assists me in comprehending the visualization of Pearson's correlation matrix. In this matrix, a correlation coefficient of <b>1 indicates a strong positive correlation</b>, <b>0 suggests a moderate correlation</b>, and <b>-1 indicates a strong negative correlation or no correlation</b>. By examining the heat map, I can quickly identify patterns and relationships between variables. This allows for a deeper understanding of the data and aids in making informed decisions based on the strength and direction of the correlations. -Histogram: The histogram assists me in comprehending the data more effectively and accurately. It provides detailed insights into the frequencies of products sold by farmers and retailers respectively. By examining the histogram, I can discern the distribution patterns of sales for each group. This allows me to identify the most common selling prices and quantities, providing valuable information for analyzing market trends and making informed decisions. Additionally, the histogram facilitates a deeper understanding of the variability and distribution of sales data, enabling more precise assessments of market dynamics
-PieChart: The pie chart provides me with a visual overview of the average spread of data across different groups. It offers a quick glance at how the data is distributed among various categories or groups. By examining the pie chart, I can easily perceive the proportion of each group relative to the whole dataset. This visualization aids in understanding the relative sizes or contributions of different categories, facilitating quick comparisons and insights into the distribution patterns of the data.

"""








#A_5: The Conclusion: Insights Unveiled
#Load and Print the First Few Rows of the Data

#Load the dataset into pandas dataframe
education_df = pd.read_csv("./Data_Sets/US_demo_graphics/Educationv.csv", index_col=0)
finance_df = pd.read_csv("./Data_Sets/US_demo_graphics/Finance.csv", index_col=0)
industry_df = pd.read_csv("./Data_Sets/US_demo_graphics/Industry.csv", index_col=0)


#Revealing the structure of data
print(f"Shape of datasets:\n Education: {education_df.shape}\n Finance: {finance_df.shape}\n Industry {industry_df.shape}")

#Introducing the dataset with the first few rows

#Priniting first few rows of education dataset
education_df.head()
#Priniting first few rows of finance dataset
finance_df.head()
#Priniting first few rows of industry dataset
industry_df.head()


#Decode Data Types of Each Columns

#Data types of education dataset
print(f"Data types of each feature in education dataset:\n{education_df.dtypes}\n {"="*100}")
#Data types of finance dataset
print(f"Data types of each feature in finance dataset:\n{finance_df.dtypes}\n{ "="*100}")
#Data types of industry dataset
print(f"Data types of each feature in industry dataset:\n{industry_df.dtypes}\n {"="*100}")


#Begin a Statistical Journey

#Stastical analysis of education dataset
print("Complete statistical analysis of my education dataset is:")
education_df.describe()

#Mapping of old col names with new col names
col_names = {
    'Less_than_$5000': 'Less_than_\\$5000',
    '$5000_to_$9999': '$5000_to_\\$9999',
    '$10000_to_$14999': '$10000_to_\\$14999',
    '$15000_to_$19999': '$15000_to_\\$19999',
    '$20000_to_$24999': '$20000_to_\\$24999',
    '$25000_to_$34999': '$25000_to_\\$34999',
    '$35000_to_$49999': '$35000_to_\\$49999',
    '$50000_to_$74999': '$50000_to_\\$74999',
    '$75000_to_$99999': '$75000_to_\\$99999',
    '$100000_to_$149999': '$100000_to_\\$149999',
    '$150000_or_more': '$150000_or_more'
}

							
#Renaming column names
finance_df = finance_df.rename(columns=col_names)

#Stastical analysis of finance dataset
print("Complete statistical analysis of my finance dataset is:")
finance_df.describe()

#Stastical analysis of industry dataset
print("Complete statistical analysis of my industry dataset is:")
industry_df.describe()


#Explorining the Relationship Between Education Data
plt.figure(figsize=(14, 6))




#Scatter plot : A Quick overview of data
#Scatter plot of education dataset
plt.scatter(education_df['Bachelors_degree_or_higher'], education_df['high_school_or_some_degree'],
            color="blue", label="Bachelors Degree Vs High School or Some Degree", alpha=0.8)
plt.scatter(education_df['Bachelors_degree_or_higher'], education_df['Less_than_high_school_graduate'],
            color="hotpink", label="Bachelors Degree Vs Less Than High Some Degree")


plt.title("Graphical Description of Data")
plt.legend()
plt.show()


#Scatter plot of finance dataset
#Compute no. of rows and no. of cols for figure
rows = finance_df.columns[1:8]
cols = finance_df.columns[8:]


fig, axes = plt.subplots(nrows=len(rows), ncols=len(cols), figsize=(15, 30))
for index1, col_name1 in enumerate(rows):
    for index2, col_name2 in enumerate(cols):
        axes[index1, index2].scatter(finance_df[col_name1], finance_df[col_name2], color="hotpink")

        #Set title and  xlabel and ylabel
        axes[index1, index2].set_xlabel(col_name1)
        axes[index1, index2].set_ylabel(col_name2)
        axes[index1, index2].grid(True)
        

plt.tight_layout()
plt.show()


#Scatter plot of industry dataset
#Assigining col names to variables
c1 = "Total_Agriculture_forestry_fishing_hunting_mining"
c2 = "Total_Construction"
c3 = "Total_Manufacturing"
c4 = "Total_Wholesale_trade"
c5 = "Total_Retail_trade"
c6 = "Total_Transportation_warehousing_utilities"
c7 = "Total_Information"
c8 = "Total_Finance_insurance_realestate_rental_leasing"

#Dividing col names into rows and cols
rows = [c1, c2, c3, c4]
cols = [c5, c6, c7, c8]


fig, axes = plt.subplots(nrows=len(rows), ncols=len(cols), figsize=(15, 30))
for index1, col_name1 in enumerate(rows):
    for index2, col_name2 in enumerate(cols):
        #Plot scatter plots
        axes[index1, index2].scatter(industry_df[col_name1], industry_df[col_name2], color="hotpink")

        #Set title and  xlabel and ylabel
        axes[index1, index2].set_xlabel(col_name1)
        axes[index1, index2].set_ylabel(col_name2)
        axes[index1, index2].grid(True)
        

plt.tight_layout()
plt.show()



#Bar Plots
#Select only float/int cols
#Group them by year and then take mean of each course
avg_student_per_course = education_df.iloc[:, 1:].groupby(['Year']).mean()
len_of_dist_years_in_edu = len(avg_student_per_course.index)


#Group them by year and then take mean of each financial year
avg_financial_price = finance_df.iloc[:, 1:].groupby(['Year']).mean()
len_of_dist_years_in_fin = len(avg_financial_price.index)


#Group them by year and then take mean of each industrial year
avg_industrial_price = industry_df.iloc[:, 1:].groupby(['Year']).mean()
len_of_dist_years_in_ind = len(avg_financial_price.index)


#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals_for_edu = np.arange(len_of_dist_years_in_edu)
equal_intervals_for_fin = np.arange(len_of_dist_years_in_fin)
equal_intervals_for_ind = np.arange(len_of_dist_years_in_ind)



#========================================Education DataSet==================================#
#Create a subplot with 1 rows and 2 columns
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

#Plot the bar graph for education dataset
multiplier = 0
for col in avg_student_per_course.columns:
    ax[0].bar(equal_intervals_for_edu + set_width * multiplier, avg_student_per_course[col], 
              width=set_width, label=col)
    multiplier += 1
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Avg. Number of Students")
ax[0].set_title('Year Vs Avg Number of Students Enrolling For Course')
ax[0].legend()
ax[0].set_xticks(equal_intervals_for_edu + set_width, avg_student_per_course.index)





#========================================Finance DataSet==================================#
#Narrowing down the dataset(finance) for ease to visulaize
avg_financial_price = avg_financial_price.iloc[:, 0:3]

#Plot the bar graph for finance dataset
multipiler = 0
for col in avg_financial_price.columns:
    ax[1].bar(equal_intervals_for_fin + set_width * multiplier, avg_financial_price[col], 
              width=set_width, label=col)
    multiplier += 1
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Avg. Finance")
ax[1].set_title('Year Vs Avg. Finance')
ax[1].legend()
ax[1].set_xticks(equal_intervals_for_fin + 1, avg_financial_price.index)
plt.show()





#========================================Industry DataSet==================================#
#Narrowing down the dataset(industry) for ease to visulaize
avg_industrial_price = avg_industrial_price.iloc[:, 0:3]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
#Plot the bar graph for industry dataset
multipiler = 0
for col in avg_industrial_price.columns:
    ax.bar(equal_intervals_for_ind + set_width * multiplier, avg_industrial_price[col], 
              width=set_width, label=col)
    multiplier += 1
ax.set_xlabel("Year")
ax.set_ylabel("Avg. Revenue")
ax.set_title('Year Vs Avg. Industrial Revenue')
ax.legend()
ax.set_xticks(equal_intervals_for_fin + 1.8, avg_financial_price.index)
plt.show()



#lluminate Correlations With a Color Plot (Heatmap)
#======================================== Co-relation In Education DataSet==================================#
#Finding co-relation amoung attributes of education dataset
correlation_matrix_edu = education_df.iloc[:, 1:].corr()
print(f"Co-relation matrix for education attributes:\n")
correlation_matrix_edu


#Plotting corealtion matrix using heatmap
plt.figure()
sns.heatmap(correlation_matrix_edu, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()


#======================================== Co-relation In Finance DataSet==================================#
#Finding co-relation amoung attributes of education dataset
correlation_matrix_fin = finance_df.iloc[:, 1:5].corr()
print(f"Co-relation matrix for finance attributes:\n")
correlation_matrix_fin


#Plotting corealtion matrix using heatmap
plt.figure()
sns.heatmap(correlation_matrix_fin, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()


#======================================== Co-relation In Industry DataSet==================================#
#Finding co-relation amoung attributes of education dataset
correlation_matrix_ind = industry_df.iloc[:, 1:5].corr()
print(f"Co-relation matrix for Industry attributes:\n")
correlation_matrix_ind


#Plotting corealtion matrix using heatmap
plt.figure()
sns.heatmap(correlation_matrix_ind, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Heatmap')
plt.show()


#Plotting Histograms
#======================================== Histogram For Education DataSet==================================#
fig, axs = plt.subplots(1, 3, figsize=(14, 6), sharey=True)

#Plotting fist historgram of bachelors degree or higer
axs[0].hist(education_df["Bachelors_degree_or_higher"], bins=50, color='skyblue', edgecolor='red')
axs[0].set_title('Bachelors Degree Distribution')
axs[0].set_xlabel('Bachelors Degree or Higer')
axs[0].set_ylabel('Frequency')
axs[0].grid(True)

#Plotting second historgram of high school or some degree
axs[1].hist(education_df["high_school_or_some_degree"], bins=50, color='orange', edgecolor='red')
axs[1].set_title('Hight School or Some Degree Distribution')
axs[1].set_xlabel('High School or Some Degree')
axs[1].grid(True)

#Plotting third historgram of less than hight school graduate
axs[2].hist(education_df["Less_than_high_school_graduate"], bins=50, color='cyan', edgecolor='red')
axs[2].set_title('Less Than High School Graduate Distribution')
axs[2].set_xlabel('Less Than Hight School Graduate')
axs[2].grid(True)



fig.suptitle('Histograms of Various Courses', fontsize=12)
plt.show()


#Craft a Histogram—observe the distribution of different variables.
#======================================== Histogram For Finance DataSet==================================#
fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(14, 35))

#Reshaping column names
col_names = np.reshape(finance_df.columns[2:], (5, 2))


for i in range(5):
    for j in range(2):
        axs[i, j].hist(finance_df[col_names[i][j]], bins=60, color="orange", edgecolor="red")
        axs[i, j].set_xlabel(col_names[i][j])
        axs[i, j].set_ylabel("Frequiency")
        axs[i, j].grid(True)
    
plt.tight_layout()
plt.show()

#======================================== Histogram For Industry DataSet==================================#
fig, axs = plt.subplots(nrows=10, ncols=2, figsize=(14, 60))

#Reshaping column names
col_names = np.reshape(industry_df.columns[2:22], (10, 2))


for i in range(10):
    for j in range(2):
        axs[i, j].hist(industry_df[col_names[i][j]], bins=60, color="cyan", edgecolor="red")
        axs[i, j].set_xlabel(col_names[i][j])
        axs[i, j].set_ylabel("Frequiency")
        axs[i, j].grid(True)
    
plt.tight_layout()
plt.show()


#Plotting PieCharts
#======================================== PieChart For Education DataSet==================================#
#Number of unique entries in each column
unique_entries = education_df.nunique(axis=0)
mylabels = education_df.columns[1:]
myexploide = [0.1, 0.1, 0.1]

#Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(unique_entries[1:], labels=mylabels, shadow=True, explode=myexploide)
plt.title("Number of Students Distribured Over Different Courses")
plt.legend(loc='upper left')
plt.show()


#======================================== PieChart For Finance DataSet==================================#
#Number of unique entries in each column
unique_entries = finance_df.nunique(axis=0)
mylabels = finance_df.columns[1:]
#Setting my explode
myexploide = np.zeros(len(mylabels) - 1) * 0.0
myexploide = np.append(myexploide, 0.2)

#Plot pie chart
plt.figure(figsize=(14, 8))
plt.pie(unique_entries[1:], labels=mylabels, shadow=True, explode=myexploide)
plt.title("Distribution of Finance")
plt.legend(loc='upper left')
plt.show()


#======================================== PieChart For Industry DataSet==================================#
#Number of unique entries in each column
unique_entries = industry_df.nunique(axis=0)
mylabels = industry_df.columns[1:]

#Plot pie chart
plt.figure(figsize=(14, 100))
plt.pie(unique_entries[1:], labels=mylabels, shadow=True)
plt.title("Distribution of Income In Industry")
# plt.legend(loc='upper left')
plt.show()


#Problem B:  See the Climate data set and load it completely using Pandas

#Load the dataset into pandas dataframe
climate_df = pd.read_excel("./Data_Sets/Climate/Climate.xlsx", index_col=0)

#Revealing the structure of data
print(f"Shape of climate datasets: {climate_df.shape}")


#Introducing the dataset with the first few rows
#Priniting first few rows of climate dataset
climate_df.head()



#Decode data types of each columns
#Data types of climate dataset
print(f"Data types of each feature in climate dataset:\n{climate_df.dtypes}\n")




#Do you see any patterns in the crop production in the area?
#It's hard to see the trends of data by seeing the textual data

#Exploring the relationship b/w Lowest and Highest Temp
#Explorining the relationship between highest and lowest temp using scatter plot
plt.figure(figsize=(14, 6))


#Scatter plot : A Quick overview of data
plt.scatter(climate_df['Month'], climate_df['Lowest Temp'],
            color="blue", label="Month Vs Lowest Temp", alpha=0.8)
plt.scatter(climate_df['Month'], climate_df['Highest Temp.'],
            color="hotpink", label="Month Vs Highest Temp", alpha=0.8)


plt.title("Graphical Description of Data")
plt.legend()
plt.show()


#Explorining the relationship between features of climate dataset using bar plots
#========================================Year Vs Avg(Hihest Temp. and Lowest Temp.)==================================#
#Group them by year and then take mean of highest temp. and lowest temp
avg_temp = climate_df.iloc[:, 2:4].groupby(['Year']).mean()
len_of_dist_years = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_years)

#Create a subplot with 3 rows and 2 columns
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(12, 14), sharey=True)

#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[0, 0].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[0, 0].set_xlabel("Year")
ax[0, 0].set_ylabel("Range")
ax[0, 0].legend()
ax[0, 0].set_xticks(equal_intervals + set_width, avg_temp.index)



#========================================Month Vs Avg(Hihest Temp. and Lowest Temp.)==================================#
#Group them by month and then take mean of highest temp. and lowest temp
avg_temp = climate_df.iloc[:, [0, 2, 3]].groupby(['Month']).mean()
len_of_dist_months = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_months)


#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[0, 1].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Range")
ax[0, 1].legend()
ax[0, 1].set_xticks(equal_intervals + set_width, avg_temp.index)



#========================================Month Vs Avg(Hihest Temp. and Paddy Production(Tonnes))==================================#
#Group them by month and then take mean of highest temp. and Paddy Production(Tonnes)
avg_temp = climate_df.iloc[:, [0, 2, 5]].groupby(['Month']).mean()
len_of_dist_months = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_months)


#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[1, 0].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Range")
ax[1, 0].legend()
ax[1, 0].set_xticks(equal_intervals + set_width, avg_temp.index)


#========================================Month Vs Avg(Lowest Temp. and Paddy Production(Tonnes))==================================#
#Group them by month and then take mean of lowest temp. and Paddy Production(Tonnes)
avg_temp = climate_df.iloc[:, [0, 3, 5]].groupby(['Month']).mean()
len_of_dist_months = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_months)


#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[1, 1].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[1, 1].set_xlabel("Month")
ax[1, 1].set_ylabel("Range")
ax[1, 1].legend()
ax[1, 1].set_xticks(equal_intervals + set_width, avg_temp.index)




#========================================Month Vs Avg(Hihest Temp. and People dying from Heat Strokes)==================================#
#Group them by month and then take mean of highest temp. and People dying from Heat Strokes
avg_temp = climate_df.iloc[:, [0, 2, 8]].groupby(['Month']).mean()
len_of_dist_months = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_months)


#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[2, 0].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[2, 0].set_xlabel("Month")
ax[2, 0].set_ylabel("Range")
ax[2, 0].legend()
ax[2, 0].set_xticks(equal_intervals + set_width, avg_temp.index)


#========================================Month Vs Avg(Lowest Temp. and People dying from Heat Strokes)==================================#
#Group them by month and then take mean of lowest temp. and People dying from Heat Strokes
avg_temp = climate_df.iloc[:, [0, 3, 8]].groupby(['Month']).mean()
len_of_dist_months = len(avg_temp.index)

#Setting width and equal intervals for xticks
set_width = 0.25
equal_intervals = np.arange(len_of_dist_months)


#Plot the bar graph
multiplier = 0
for col in avg_temp.columns:
    ax[2, 1].bar(equal_intervals + set_width * multiplier, avg_temp[col], 
              width=set_width, label="Avg. " + col)
    multiplier += 1
ax[2, 1].set_xlabel("Month")
ax[2, 1].set_ylabel("Range")
ax[2, 1].legend()
ax[2, 1].set_xticks(equal_intervals + set_width, avg_temp.index)

plt.show()


# - With ease we can observe the trends in data set, like with incresing temp. people dying with heat strokes
# increases, and much more

