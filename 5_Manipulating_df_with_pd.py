import os
import pandas as pd
import numpy as np
# os.system("pwd")

file_path = []
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Data_Analysis/Dataset"):
    for filename in filenames:
        file_path.append(os.path.join(dirname, filename))

# print(file_path)
data = pd.read_csv(file_path[1]) # pokemon.csv
print(data.head())

### Manipulating Data Frames With Pandas
## Indexing Data Frames
# - Indexing using square brackets
# - Using column attribute and row label
# - Using loc accessor
# - Selecting only some columns

# square brackets을 활용한 indexing 조회
# 먼저 #라는 attribute를 행index으로 매기자
data = data.set_index("#")
print(data.head())
print(data["HP"][1]) # <- [n] 은 여기서 indexing 행 번호를 따른다. 별도의 set_index가 없다면, [0]부터 시작

# using column attribute and row label (column attribute[행 index(또는 라벨)] 로 접근하기)
print(data.HP[1])

# using loc accessor (loc 메소드로 조회)
print(data.loc[1, ["HP"]]) # loc은 조금더 자세히 조회해준다.

# Selecting only some columns
print(data[["HP", "Attack"]].head()) # data frame type

## Slicing Data Frame
# - Difference between selecting columns
#   - Series and data frames
# - Slicing and indexing series
# - From something to end

# Difference between selecting columns (Series & Dataframe)
print(type(data["HP"])) # Series 형태로 조회
print(type(data[["HP"]])) # Dataframe 형태로 조회

# Slicing and indexing series
print(data.loc[1:10, "HP":"Defense"]) # boundary도 포함
# + Reverse Slicing
print(data.loc[10:1:-1, "HP":"Defense"]) # .loc[시작:끝:interval, - - -] : interval은 생략가능하다. default = +1
 
# From somthing to end
print(data.loc[1:10, "Speed":]) # Speed라는 column attribute부터 쭈욱--!

## Filtering Data Frames
# - Creating boolean series 
# - Combining filters 
# - Filtering column based others.

# Creating boolean series
boolean = data.HP > 200 # boolean series type
print("data['HP'][boolean] : ")
print(data["HP"][boolean])  # HP Series satisfying the boolean condition

print("data[boolean] : ")
print(data[boolean]) # Data Frame with rows satisfying the boolean condition

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
print("data[first_filter & second_filter] : ")
print(data[first_filter & second_filter])
# or with np.logical_and(A, B)
print("\n data[np.logical_and(first_filter, second_filter)] : ")
print(data[np.logical_and(first_filter, second_filter)])

# Filtering column based others
print("\ndata.HP[data.Speed<15] : ")
print(data.HP[data.Speed<15]) # 다른 조건을 적용한 원하는 열 정보만 출력

## Transforming Data (데이터 변환)
# - Plain python functions
# - Lambda function : to apply arbitrary python function to every element
# - Defining column using other columns

# Plain python functions (평범한 파이썬 함수)
def div(n):
    return n/2

print("\ndata.HP.apply(div) : ")
print(data.HP.apply(div)) # .apply 메소드를 통해 series의 모든 데이터에 어떤 함수를 적용시킬 수 있다.

# Lambda inline function (more faster)
print("\ndata.HP.apply(lambda n: n/2) : ")
print(data.HP.apply(lambda n: n/2))

# Defining new column using other columns (다른 기존 열들을 연산하여 새로운 결과 열 정의하기)
data["total_power"] = data.Attack + data.Defense
print(data.head())

## Index Objects & Labeled Data
# Our index name is this : ( Pandas 에서 index란 행 라벨을 말하는 것이다. set_index로 지정할 수 있다.)
print(data.index.name)
# lets change it
data.index.name = "index_name" # df.index.name 으로 접근해서 index 이름변경이 가능하다.
print(data.head())

# Overwrite index ( 인덱스 값을 바꾸고 싶을 때, df.index 로 접근해서 변경하면 된다. )
# iterable generator 를 적용할 수 있다.
# ex) data3 = data.copy()
#     data3.index = range(100,900,1) # 인덱스가 100부터 시작하게 됨. 
# 또는 기존에 알고 있듯이 
# df.set_index("#") 로 열을 인덱스로 지정해줄 수도 있고,
# 또는 df.index = df["#"] 로 해줄 수도 있다.

## Hierarchical Indexing (계층적 인덱싱)
data = pd.read_csv(file_path[1]) # pokemon.csv
print(data.head())
# Setting Indexing : type 1 is outer, type 2 is inner index
data1 = data.set_index(["Type 1", "Type 2"]) # 그룹끼리 묶어서 계층을 형성시켜 인덱싱한다.
print(data1.head(100)) 
# print(data1.loc["Fire", "Flying"]) # hierarchical indexing 일 때 loc조회 방법 (자세히 살펴볼 것)

## Pivoting Data Frames
# pivoting : reshape tool
dic = {"treatment" : ["A", "A", "B", "B"], "gender" : ["F","M","F","M"], "response" : [10,45,5,9], "age" : [15,4,72,65]}
df = pd.DataFrame(dic) # dictionary를 data frame으로 바꾸기.
print(df)

# pivoting
print(df.pivot(index="treatment", columns="gender", values="response"))
# df.pivot : 두 개의 변수값에 따라 다른 값이 어떻게 가지는 지 살펴보기에 유용함.
# pd.pivot_table(df, index=, columns=, values=)를 써도 좋다.
# pd.pivot_table의 장점은 aggfunc=np.mean, margins=True 추가 옵션을 통해서 
# 행/열별 연산 결과를 같이 출력할 수 있다.

## Stacking & Un-Stacking Data Frame
# - deal with multi label indexes
# - level : position of unstacked index
# - swaplevel : change inner and outer level index position
df1 = df.set_index(["treatment", "gender"]) # hierarchical indexing
print(df1) 

# lets Un-stack it.
# level determines indexes
print(df1.unstack(level=0)) # level 이 낮을 수록 Outer index를 unstack 하겠다는 말이다.
# unstack 된 index는 모든 열에 적용된다.

# change inner and outer level index position
df2 = df1.swaplevel(0,1) # 현재 hierarchical indexing 된 df의 index레벨을 서로 바꾼다. 
print(df2)

## Melting Data Frames
# - Reverse of Pivoting 
print(df)

print(pd.melt(df, id_vars="treatment", value_vars=["age", "response"]))

## Categoricals & Groupby
print(df)

# According to treatment, take means of other features.
# treatment에 따라 그룹화하여 aggregation/reduction method를 적용한다. 
# 이 때 aggregation/reduction method가 적용되지 않는 attribute columns들은 알아서 빠진다.
print("\ndf.groupby('treatment').mean() : ")
print(df.groupby("treatment").mean())

# Or we can only choose one of the features.
print('\ndf.groupby("treatment").age.mean() : ')
print(df.groupby("treatment").age.mean())

# Or we can choose multiple features.
print('\ndf.groupby("treatment")[["age", "response"]].min() : ')
print(df.groupby("treatment")[["age", "response"]].min()) # 여러 개 features를 선정하여 그룹별 최소값(min)을 뽑아냄

print(df.info())
# as you can see gender is object
# However if we use groupby, we can convert it categorical data. 
# Because categorical data uses less memory, speed up operations like groupby
# df["gender"] = df["gender"].astype("category")
# df["treatment"] = df["treatment"].astype("category")
# print(df.info())