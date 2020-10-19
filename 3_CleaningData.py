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
# 일반적으로 Outlier는 Q1 - 1.5 * IQR 보다 작거나, Q3 + 1.5 * IQR 보다 큰 값들을 Outlier로 처리한다. 

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
# id_vars = what we don't wish to melt, but want to concern.
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
# concat하고 나면 지들 자체적으로 또 '자체'인덱스를 매기게 되는데, 이 때
# pd.concat(ignore_index=True)를 하게되면, 자체인덱스는 합쳐진 두 dataframe내에서 사용하던
# 인덱스에 의존하지 않는다. (False로 하면, 자체인덱스가 데이터 행 넘버를 따라가게 된다.)
# Default는 ignore_index=False이다.
# axis = 0 : adds dataframes in row. (행 방향으로 엮음)
print(conc_data_row)

data1 = data['Attack'].head() # Series
data2 = data['Defense'].head() # Series
conc_data_col = pd.concat([data1, data2], axis=1)
# axis = 1 : add dataframes in column (열 방향으로 엮음)
print(conc_data_col)


## Data Types
# There are 5 basic data types : object(string), boolean, integer, float, and categorical.
# We can make conversion data types like from str to categorical or from int to float
# Why is categorical data type important?
# - Make dataframe smaller in memory. (카테고리형 데이터타입은 메모리를 더 적게 먹는다.)
# - Can be utilized for analysis especially for sklearn(we will learn later) 
#    (분석, 특히 sklearn분석, 활용에 유용한 데이터타입 이다.)
print("data.dtypes : ")
print(data.dtypes)

# Lets convert object(str) to categorical & int to float.
data['Type 1'] = data['Type 1'].astype('category') # astype("변환할 데이터타입")
data['Speed'] = data['Speed'].astype('float')

print("astype이후의 data.dtypes : ")
print(data.dtypes) 
# As you can see, Type 1 is converted from object to categorical
# And Speed is converted from int to float.

## Missing Data & Testing with Assert
# If we encounter with missing data, what we can do :
# - leave as is  (1. 그대로 놔둔다.)
# - drop them with dropna() (2. 해당하는 항목은 drop해버려서 취급하지 않는다.)
# - fill missing value with fillna() (3. fillna()를 통해 뭔가를 채워넣는다.)
# - fill missing values with test statistics like mean (4. 평균과 같은 통계치를 활용해 채워넣는다.)
# Assert statement : check that you can turn on or turn off 
#                    when you are done with your testing of the program
# Python Assert statement : 파이썬 가정설정문 이라고 한다. 예외처리(exception)와 비슷한 성격
# Assert statement 는 단순히 에러는 찾는 것 뿐아니라, 값을 보증하기 위해서도 사용된다.
# 예를 들어, 함수의 입력 값이 어떤 조건의 True임을 '보증'하기 위해서 Assert statement를 사용하기도 한다.
#          이처럼 실수를 가정해서 '값을 보증하는 방식'으로 코딩하기 때문에 '방어적 프로그래밍'이라 부른다.
# (원하는 값이 아니라면 AssertionError : 를 발생시킨다.)

# Lets look at does pokemon data have nan value ( 포켓몬 데이터가 nan 값을 어떻게 가지고 있는지 보자 )
print("data.info() : ")
print(data.info())
# As you can see, there are 800 entries. However, Type 2 has 414 non-null object 
# so it has 386 null object!! OMG, it is almost a half of all entries.

# Lets check Type 2
print("data['Type 2'].value_counts(dropna=False) : ")
print(data["Type 2"].value_counts(dropna=False))
# As you can see, there are 614 non-null value & 386 NAN value.

# Lets drop NAN values
data1 = data
data1['Type 2'].dropna(inplace=True) 
# inplace = True  means we do not assign it to new variable. (새로운 variable을 만들어 할당하지 않겠다는 뜻이다.)
# Changes automatically assigned to data. (즉, 기존데이터에 적용하겠다는 뜻이다.)
# 다시 말해, data2 = data1['Type 2'] ~~ 이런 식으로 새로운 변수를 선언할 필요가 없어.
# inplace=True 로 인해, 변화가 기존 데이터에 덮어 씌워진다.
# So does it work?
# Lets check with assert statement
# assert 1 == 1 # return nothing because it is always true.
print("data['Type 2'].notnull() : ")
print(data['Type 2'].notnull()) # .notnull() 메소드 : 값이 non-null이면 True를 반환.
assert data['Type 2'].notnull().all() # (True)return nothing because we drop NAN values.
# .all() 파이썬 빌트인 메소드 : 모든 값이 True면, True 반환.
print("Check Again : ")
print(data['Type 2'].value_counts(dropna=False)) # 414개만 뜸 (nan values들은 전부 drop해버렸기 때문에.)

# Ver2. : Fill nan value with certain values. fillna()
# data['Type 2'].fillna('empty', inplace=True) # 마찬가지로 inplace=True로, variable 따로 필요없다.
# assert data['Type 2'].notnull().all() # returns nothing because we don't have nan values.
# Assert statement 는 일종의 '보증'의 역할을 수행하는 것이다. NaN value가 없음을 보증!
# With assert statement we can check a lot of thing. For example,
# assert data.columns[1] == 'Name'
## print(data.columns[1]) -> Name (두 번째 argument)
# assert data.Speed.dtypes == np.int 

