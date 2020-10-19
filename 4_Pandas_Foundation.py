## PANDAS FOUNDATION 판다스 기초
# single column = Series
# NaN = Not a Number
# dataframe.values = Numpy (np)

# Building Data Frames From SCRATCH
# - We can build data frames from csv as we did earlier.
# - 'Also' we can build dataframe from "dictionaries"
#    - zip() method : This function returns a list of tuples, where
#                     the i-th tuple contains the i-th element from each
#                     of the argument sequences or iterables.
# - Adding new column
# - Broadcasting : Create new column and assign a value to entire columns.
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
# %matplotlib inline

# data frames from dictionary.
country = ["Spain", "France"]
population = ["11", "12"]
list_label = ["country", "population"]
list_col = [country, population]
zipped = list(zip(list_label, list_col))
print("zipped : ")
print(zipped) # [('country', ['Spain', 'France']), ('population', ['11', '12'])]
data_dict = dict(zipped)
print("dict(zipped) : ")
print(data_dict) # {'country' : ['Spain', 'France'], 'population' : ['11', '12']}
df = pd.DataFrame(data_dict)
print(df)

# Add new columns
df["capital"] = ["madrid", "paris"]
print(df)

# Broadcasting
df["income"] = 0 # Broadcasting entire column
print(df)

## Visual Exploratory Data Analysis 시각화를 활용한 탐색적 데이터 분석(EDA)
# Plot
# Subplot
# Histogram :
# - bins : number of bins
# - range(tuple) : min and max values of bins
# - normed(boolean) : normalize or not
# - cumulative(boolean) : compute cumulative distribution

# Plotting all data

csv_path = []
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Data_analysis/Dataset"):
    for filename in filenames:
        csv_path.append(os.path.join(dirname, filename))

for csv in csv_path:
    if "pokemon" in csv:
        data = pd.read_csv(csv)
    else:
        continue

data1 = data.loc[:, ['Attack', 'Defense', 'Speed']]
## plot
# data1.plot() # need to execute this python script itself.
# plt.show()

## subplots
# data1.plot(subplots=True) # columns 별로 따로따로 다 보여준다.
# plt.show()

## scatter plot
# data1.plot(kind='scatter', x='Attack', y='Defense')
# plt.show()

## hist plot
# data1.plot(kind='hist', y='Defense', bins=50, range=(0,250), normed=True)
# plt.show()

## histogram subplot with non-cumulative & cumulative
# fig, axes = plt.subplots(nrows=2, ncols=1)
# data1.plot(kind='hist', y='Defense', bins=50, range=(0,250), normed=True, ax=axes[0])
# data1.plot(kind='hist', y='Defense', bins=50, range=(0,250), normed=True, ax=axes[1], cumulative=True)
# - cumulative histogram은 "어느 순간에 비중이 급증하는가" 를 한 눈에 파악할 수 있는 좋은 histo type이다.
# plt.show()

# ---------------
## Statistical Exploratory Data Analysis 통계를 활용한 탐색적 데이터 분석(EDA)
# count, mean, std, min, 25%(Q1), 50%(Q2), 75%(Q3), max
print(data.describe())

## Indexing Pandas Time Series
# datetime = object
# parse_dates(boolean) : Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss) format.
time_list = ["1992-03-08", "1992-04-12"]
print(type(time_list[1])) # As you already know, this is type of string(str)
# However, we want it to be 'datetime' object.
datetime_object = pd.to_datetime(time_list)
print("type(datetime_object) : ")
print(type(datetime_object))

print("datetime_object : ")
print(datetime_object) # DatetimeIndex(['1992-03-08', '1992-04-12'], dtype='datetime64[ns]', freq=None)

# close warning
import warnings
warnings.filterwarnings("ignore")

data2 = data.head()
date_list = ["1992-01-10", "1992-02-10", "1992-03-10", "1993-03-15", "1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2['date'] = datetime_object
# lets make date as index (data2의 date란 column을 행 index로 매긴다.)
data2 = data2.set_index("date")
print("data2 : ")
print(data2)

# Now we can select according to our date index. (이제 date인덱스를 통해서 조회를 할 수 있다는 말)
print("data2.loc['1993-03-16'] : ")
print(data2.loc["1993-03-16"])

print("data2.loc['1992-03-10' : '1993-03-16'] : ")
print(data2.loc["1992-03-10" : "1993-03-16"])

## Resampling Pandas Time Series
# Resampling : statiscal method over different time intervals
# - Needs string to specify frequency like "M" : month or "A" : year
# Downsampling : reduce date time rows to slower frequency like from daily to weekly
# Upsampling : increase date time rows to faster frequency like from daily to hourly
# Interpolate : interpolate values according to different methods like "linear", "time" or "index".
# - ref : https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.interpolate.html

# "A" : year ; data2를 연도로 묶어 resampling한다. 그 후 그룹끼리 평균(mean)한 df를 보여준다.
print("data2.resample('A').mean() : ") 
print(data2.resample("A").mean())

# Lets resample with month // "M" : month; data2를 월단위로 묶어 resampling한다. 그 후 그룹끼리 평균(mean)한 df를 반환한다.
print("data2.resample('M').mean() : ")
print(data2.resample("M").mean())
# As you can see, there are a lot of 'NaN' because data2 does not include all months.

# In real life (Not created from us like data2), we can solve this problem
# with 'interpolate'. (실제 실무에서는 이런 문제를 만났을 때, interpolate를 써서 해결할 수 있다.)
# Lets resample from first value (아! resample을 하되 가장 먼저오는(first) 값(value)을 대표값으로 쓰겠다는 방법론이다.)
# 또한! interpolate는 아예 해당 데이터가 없을 경우에 존재하는 값 사이를 linear하게 쪼개서 값을 채워넣는다.
print("data2.resample('M').first().interpolate('linear') : ")
print(data2.resample("M").first().interpolate("linear"))

# Or we can interpolate with mean()
# ! mean()으로 resampling하면 int나 float같은 numeric type이 아닌 타입의 열은 제외시키고 반환한다.
print('data2.resample("M").mean().interpolate("linear") : ')
print(data2.resample("M").mean().interpolate("linear"))