## 3. CLEANING DATA
# Diagnose data for CLEANING(정제를 위한 우선적인 데이터 진단)
# 분석 전, 불순하거나 불완전한 데이터를 지우거나 처리하는 과정이다. (전처리)
# Unclean data :
# 1. Column name inconsistency like upper-lower case letter or space between words.
#    (열 이름의 일관성 : 대소문자 혼합, 또는 단어 사이의 공백같은..)
# 2. missing data ( N/A 같은 것들 )
# 3. different language + Outlier(이상치)
#
# We will use Pandas's head, tail, columns, shape, info methods to diagnose data.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print(os.system("pwd"))
csv_path = []
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Data_analysis/Dataset"):
    for filename in filenames:
        csv_path.append(os.path.join(dirname, filename))

# print(csv_path)
for csv in csv_path:
    if "pokemon" in csv:
        data = pd.read_csv(csv)
    else:
        continue

print("head shows first 5 rows : data.head()")
print(data.head())

print("tail shows last 5 rows : data.tail()")
print(data.tail())

print("columns gives column names of features : data.columns")
print(data.columns)

print("shape gives number of rows and columns in a tuple : data.shape")
print(data.shape) # data is shaped of (800 rows, 12 cols).

print("""info gives data type like dataframe, number of sample or row, number of feature or column,
feature types and memory usage : data.info()""")
print(data.info()) ## ** Non-null count도 해준다. 그래서 diagnose data 하기 유용한 method이다.

## Exploratory Data Analysis (탐색적 데이터 분석)
# 수집한 데이터를 다양한 각도(시각적그래프, 기초통계적분석)에서 관찰하고 이해하는 과정.
# 데이터를 본격 분석하기 전 수행된다. 그래프나 통계적인 방법으로 데이터를 직관적으로 바라보는 과정이다.
# 25% : first quantile*(Q1)
# 50% : median or second quantile(M or Q2)
# 75% : third quantile(Q3)
# Q3-Q1 = IQR(the Interquartile Range) = 중앙값에서 양옆으로 50%를 차지하는 범위.
print("For example lets look 'frequency' of pokemon types1 : ")
print(data['Type 1'].value_counts(dropna=False))
# value_counts(dropna=True/False) : True - Nan value not count (말그대로 drop해버림)
#                                   False - Nan value도 따로 같이 count함.

# 사분위수와 기본적인 통계량을 출력해주는 describe() 메소드.
print(data.describe()) # ignore null entries : nan value들이나 null값들은 계산에 포함시키지 않음.


## VISUAL EXPLORATORY DATA ANALYSIS (시각화를 이용한 탐색적 데이터 분석)
# 1. Box plots : visualize basic statistics like outliers, min/max or quantiles.
# Black line at top is max
# Blue line at top is 75%(Q3)
# Green line is median(50%; Q2)
# Blue line at bottom is 25%(Q1)
# Black line at bottom is min

data.boxplot(column="Attack", by="Legendary") ## by="Legendary" 옵션을 달면 그림이 False and True로 나오는데
                                               # 무슨 의미인지 잘 모르겠음!!
                                               # 아! Legendary 라는 column이 있음!!
# plt.show()

## TIDY DATA : tidy (단정한, 말쑥한, 정돈하다, 가지런하게 하다.)
# We tidy data with melt(). Describing melt() is confusing.
# Therefore lets make example to understand it.
# Firstly I create new data from pokemons data to explain 'melt()' more easily.
data_new = data.head()
print(data_new)

# lets melt.
# id_vars = what we don't wish to melt.
# value_vars = what we want to melt.
melted = pd.melt(frame=data_new, id_vars='Name', value_vars=['Attack', 'Defense'])
print(melted)
print("And melted's type is : ", type(melted)) # -> <class 'pandas.core.frame.DataFrame'>

## PIVOTING DATA : Reverse of melting.
# Index is name
# I want to make that columns are variable
# Finally, values in column are value.
print(melted.pivot(index='Name', columns='variable', values='value'))
# melt한 대상의 variable을 columns으로 나열시키고,
# values는 melt의 variable의 값들로 채운다!

## Concatenating Data : Concatenate (쇠사슬로 엮다, 연결하다.) - 데이터 엮기(?)
# We can concatenate two dataframe. (두 개의 데이터 프레임을 하나의 프레임으로 엮는거)
# Firstly we create 2 data frame samples.
data1 = data.head()
data2 = data.tail()
# concatenate!! -> pd.concat()
conc_data_row = pd.concat([data1, data2], axis=0, ignore_index=True)
# concat하고 나면 지들 자체적으로 또 인덱스를 매기게 되는데,
# pd.concat(ignore_index=True)를 하게되면, 합쳐진 두 dataframe내에서 사용하던
# 인덱스에 의존하지 않는다.
# Default는 ignore_index=False이다.
# axis = 0 : adds dataframes in row. (행 방향으로 엮음)
print(conc_data_row)

data1 = data['Attack'].head() # Series
data2 = data['Defense'].head() # Series
conc_data_col = pd.concat([data1, data2], axis=1)
# axis = 1 : add dataframes in column (열 방향으로 엮음)
print(conc_data_col)


print()
