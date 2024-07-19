# -*- coding: utf-8 -*-
"""Online_Digital_Marketing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CnOffah05egPHYhfMAU5rnbJrKI_ojE1

#PROBLEM STATEMENT

Online Advertising Performance Data

The dataset provides insights into the online advertising performance of a company, referred to as "Company X", from April 1, 2020, to June 30, 2020. The currency used for transactions is the US dollar.

# Initial Data Understanding

Importing the necessary Python Libraries:
*   Pandas
*   Numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/online_advertising_performance_data.csv')

df.head(10)

df.shape

df.describe()

df.nunique()

df.isnull().sum()

df.drop(['Unnamed: 12'],axis=1,inplace=True)

df.drop(['Unnamed: 13'],axis=1,inplace=True)

df.shape

df['month'].unique()

df['placement'].unique()

df['placement'].value_counts()

"""Handling Null values"""

df['placement'] = df['placement'].fillna(df['placement'].mode()[0])

df.isnull().sum()

df.head(20)

df.duplicated().sum()

df.drop_duplicates(keep='first',inplace=True)

df.duplicated().sum()

df.shape

#Label Encoding
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['user_engagement']= label_encoder.fit_transform(df['user_engagement'])
df['user_engagement'].unique()

#High - 0
#Low - 1
#Medium - 2

df['campaign_number']=label_encoder.fit_transform(df['campaign_number'])

df['banner'].value_counts()

df['banner']=label_encoder.fit_transform(df['banner'])

df['placement']=label_encoder.fit_transform(df['placement'])

df['month']=label_encoder.fit_transform(df['month'])

df.head()

df.info()

"""**Question No 1: •	What is the overall trend in user engagement throughout the campaign period?**

**Solution:** <br/>
 We could see the trendlines of user engagement being almost similar and maintaining same trend for the months of April and May around value of 1, while in june although the trend is continued the same throughout all days of the month, the value i shifted and concentrated around 1.1 .
"""

campaign_period = df.groupby('day')['user_engagement'].mean().reset_index()

campaign_period = df.groupby('day')['user_engagement'].mean().reset_index()
sns.lineplot(x='day',y='user_engagement',data=campaign_period)
plt.title("User Engagement")
plt.show()

"""**Qn2	How does the size of the ad (banner) impact the number of clicks generated?**

**Insight:** <br/>
Banner size one impacted the most, while banner size 3 had contributed to the least impact of clicks generated
"""

fig = plt.figure(figsize = (10, 5))

sns.barplot(x='banner',y='clicks',data=df)
plt.title("Size of Banner v/s clicks")
plt.show()

"""**Qn3: Which publisher spaces (placements) yielded the highest number of displays and clicks?**

**Solution:** <br/>
Placement type 4 highest yield in terms of display

**Solution:**<br/>
While Placement type 2 highest yield in terms of clicks
"""

plt.figure(figsize=(15,10))
sns.barplot(y='displays',x='placement',data=df, color='green')
plt.title("Placement v/s displays")
plt.show()

plt.figure(figsize=(15,10))
plt.title("Placement v/s clicks")
sns.barplot(y='clicks',x='placement',data=df)
plt.show()

placement_agg = df.groupby('placement')[['displays', 'clicks']].sum().reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(x='placement', y='displays', data=placement_agg)
plt.title('Total Number of Displays for Each Placement')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(14, 8))
sns.barplot(x='placement', y='clicks', data=placement_agg)
plt.title('Total Number of Clicks for Each Placement')
plt.xticks(rotation=45)
plt.show()

"""**Qn 4:Is there a correlation between the cost of serving ads and the revenue generated from clicks?**

**Solution:** <br/>
Cost has a correlation score of 0.76 with revenu generated
"""

fig, ax = plt.subplots(figsize=(10,10))
plt.title('Correlation between Cost and Revenue')
ax=sns.heatmap(df.corr(),annot=True,square=1,cmap='Blues',annot_kws={'size': 7},linewidths=2,
                linecolor='yellow')

"""**Qn 5: •	What is the average revenue generated per click for Company X during the campaign period?**

**Solution:** <br/>Below is the average revenue calculation:
"""

total_reve_day = df.groupby('day')['revenue'].sum()
total_clicks = df.groupby('day')['clicks'].sum()
print(total_reve_day/total_clicks)

total_revenue_per_month=df.groupby('month')['revenue'].sum()

total_clicks_per_month=df.groupby('month')['clicks'].sum()

total_revenue_per_month/total_clicks_per_month

"""**qn6: •	Which campaigns had the highest post-click conversion rates?**

**Solution:** <br/>Below is the campaigns wise post-click conversion rates
"""

df['conversion_rate'] = df['post_click_conversions'] / df['clicks']
campaign_conversion_rates = df.groupby('campaign_number')['conversion_rate'].mean().sort_values(ascending=False)
print(campaign_conversion_rates)

"""**qn 7 •	Are there any specific trends or patterns in post-click sales amounts over time?**

**Solution:** <br/>There is a steady decline trend for post_click_sales over the date
"""

daily_sales = df.groupby('day')['post_click_sales_amount'].sum().reset_index()

plt.figure(figsize=(14, 6))
sns.lineplot(x='day', y='post_click_sales_amount', data=daily_sales)
plt.title('Trends in Post-Click Sales Amounts Over Time')
plt.xticks(rotation=45)
plt.show()

"""**Qn 8 •	How does the level of user engagement vary across different banner sizes?**

**Solution:** <br/>
Below is the ditribtuion of user engagement versus banner size
"""

plt.figure(figsize=(14, 6))
sns.countplot(hue='user_engagement', x='banner', data=df)
plt.title('User Engagement Across Different Banner Sizes')
plt.xlabel('Banner Size')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(14, 6))
sns.countplot(x='user_engagement', hue='banner', data=df)
plt.title('User Engagement Across Different Banner Sizes')
plt.xlabel('User Engagement Level')
plt.ylabel('Count')
plt.show()

df.head(5) # for reference for below set of questions

"""**Qn9 •	Which placement types result in the highest post-click conversion rates?**"""

conversion_distribution = df.groupby('placement')['post_click_conversions'].sum()

print(conversion_distribution)

"""**Qn: 10 •	Can we identify any seasonal patterns or fluctuations in displays and clicks throughout the campaign period?**

**Solution:**<br/>
Declining trend for both displays and clicks throught campaign period
"""

monthly_trends = df.groupby('day')[['displays', 'clicks']].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)

sns.lineplot(x='day', y='displays', data=monthly_trends, marker='o')
plt.title('Throught time period Trend in Displays')
plt.xlabel('day')
plt.ylabel('Total Displays')

plt.subplot(1, 2, 2)
sns.lineplot(x='day', y='clicks', data=monthly_trends, marker='o')
plt.title('Throughout Time period Trend in Clicks')
plt.xlabel('day')
plt.ylabel('Total Clicks')

plt.show()

"""**Qn11 : Is there a correlation between user engagement levels and the revenue generated?**

**Solution:** <br/>There is a negative correlation between user engagement and revenue generated
"""

fig, ax = plt.subplots(figsize=(10,10))
ax=sns.heatmap(df.corr(),annot=True,square=1,cmap='Greens',annot_kws={'size': 7},linewidths=2,
                linecolor='black')

"""**Qn12 : •	Are there any outliers in terms of cost, clicks, or revenue that warrant further investigation?**

**Solution:** <br/>Yes, there are some outliers, but they are neither big outliers, nor outliers by massive margins.They are almost closer to median and close to each other
"""

plt.figure(figsize=(15,12))
sns.boxplot(x=df['cost'],data=df)

plt.figure(figsize=(15,12))
sns.boxplot(x='clicks',data=df)

plt.figure(figsize=(15,12))
sns.boxplot(x=df['revenue'],data=df)

df.describe()

"""**Qn 13 :How does the effectiveness of campaigns vary based on the size of the ad and placement type?**

**Solution:** <br/>Below is the distribution of effectiveness of campaign based on banner and placement
"""

effectiveness_size_placement =df.groupby(['campaign_number','banner','placement'])['post_click_conversions'].mean().reset_index()
effectiveness_size_placement_sorted = effectiveness_size_placement.sort_values('post_click_conversions',ascending=False)
print(effectiveness_size_placement_sorted)

effectiveness_size_placement =df.groupby(['campaign_number','banner','placement'])['post_click_conversions'].mean().reset_index()
sns.barplot(x='banner', y='post_click_conversions', hue='placement', data=effectiveness_size_placement)
plt.title('Post-Click Conversions by Banner Size and Placement Type')
plt.xlabel('Banner Size')
plt.ylabel('Average Post-Click Conversions')
plt.show()

"""**Qn 14. Are there any specific campaigns or banner sizes that consistently outperform others in terms of ROI?**

**Solution:**<br/>
ROI Calculation
"""

df['ROI'] = (df['revenue'] - df['cost']) / df['cost']

roi_by_campaign_banner = df.groupby(['campaign_number', 'banner'])['ROI'].mean().reset_index()
roi_by_campaign_banner_sorted = roi_by_campaign_banner.sort_values('ROI', ascending=False)
print(roi_by_campaign_banner_sorted)

"""**Qn15: •	15.What is the distribution of post-click conversions across different placement types?**

**Solution:** Distribution of poct-click conversions across placement types
"""

sns.barplot(x='placement',y='post_click_conversions',data=df,palette='Set2', estimator = np.mean)
plt.title('Distribution of Post-Click Conversions Across Different Placement Types')
plt.show()

"""**Qn16•	Are there any noticeable differences in user engagement levels between weekdays and weekends?**

**Insight:**<br/>
User engagement are almost same across the weekdays and weekends
"""

user_engagements_across_days = df.groupby('day_of_week')['user_engagement'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='day_of_week', y='user_engagement', data=user_engagements_across_days)
plt.title('User Engagement by Day of Week')
plt.xlabel('Day of Week (0 = Monday, 6 = Sunday)')
plt.ylabel('Average User Engagement')
plt.show()

df.groupby('day_of_week')['user_engagement'].mean()

"""**Qn •	17.How does the cost per click (CPC) vary across different campaigns and banner sizes?**

**Solution:**<br/>
Below represents the distribution of Cost per click across campaign number and banner sizes
"""

df['CPC'] = df['cost'] / df['clicks']
sns.barplot(x='campaign_number', y='CPC', hue='banner', data=df)
plt.title('Cost Per Click (CPC) Across Different Campaigns and Banner Sizes')
plt.show()

"""**Qn •	18.Are there any campaigns or placements that are particularly cost-effective in terms of generating post-click conversions?**

**Solution:** <br/>
Campaign number 0 and placement 0  have a Cost_per_conversion of 0.163 which is cheapest
"""

df['cost_per_conversion'] = df['cost'] / df['post_click_conversions']
df['cost_per_conversion'].replace([np.inf, -np.inf], np.nan, inplace=True)
cost_effectiveness = df.groupby(['campaign_number', 'placement'])['cost_per_conversion'].mean().reset_index()
cost_effectiveness_sorted = cost_effectiveness.sort_values('cost_per_conversion',ascending=True)
print(cost_effectiveness_sorted)

post_click_acros_days = df.groupby(['month','day'])['post_click_conversions'].sum().reset_index()
sns.lineplot(x='day', y='post_click_conversions', hue='month', data=post_click_acros_days)
plt.title('Post-Click Conversions Across Days')
plt.xlabel('Day')
plt.ylabel('Post-Click Conversions')
plt.show()

"""**Qn19. Can we identify any trends or patterns in post-click conversion rates based on the day of the week?**"""

df['day_of_week'] = (df['day'] - 1) % 7
#0- sunday
#1-monday
#2-tuesday
#3-wednesday
#4-thursday
#5-friday
#6-saturday

daily_conversion_rates = df.groupby('day_of_week')['post_click_conversions'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='day_of_week', y='post_click_conversions', data=daily_conversion_rates)
plt.title('Post-Click Conversion Rates by Day of Week')
plt.xlabel('Day of Week (0 = Monday, 6 = Sunday)')
plt.ylabel('Average Post-Click Conversion Rate')
plt.show()

"""**Qn20. How does the effectiveness of campaigns vary throughout different user engagement types in terms of post-click conversions?**

Solution: <br/>
Below gives the barplot for effectives via parameters like user_engagement and post_click_conversions
"""

campaign_engagement_conversions = df.groupby(['campaign_number', 'user_engagement'])['post_click_conversions'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='campaign_number', y='post_click_conversions', hue='user_engagement', data=campaign_engagement_conversions)
plt.title('Post-Click Conversions by Campaign and User Engagement Level')
plt.xlabel('Campaign Number')
plt.ylabel('Average Post-Click Conversions')
plt.show()

df.info() #reference

