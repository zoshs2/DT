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
# 