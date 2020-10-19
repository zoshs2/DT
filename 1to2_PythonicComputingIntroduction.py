# conda env : ds1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns ## visualization tool
## Directory Tree on/off : cmd + \ (ATOM editor 기준)
## Shortcut to hide the sidebar in VSCODE : cmd + b

import os
## os.system("pwd")

csv_path = []
for dirname, _, filenames in os.walk("/Users/yungi/Documents/Hello_Atom/Data_analysis/Dataset"):
    ## "os.walk" returns dirname of os.walk("dirname") accepted by itself
    ## and returns list(filenames) with including files' names.
    for filename in filenames:
        ## print(dirname)
        # print(os.path.join(dirname, filename))
        csv_path.append(os.path.join(dirname, filename))
        ## "os.path.join" does not care about the existence of slash(/) or not.
        ## It just makes the given path be proper.

# print(csv_path)
while True:
    for csv in csv_path:
        if "pokemon" in csv:
            read_csv = csv
            print(read_csv)
            data = pd.read_csv(read_csv)
            break
        else:
            continue
    break

# print(type(data))
print(data.head()) # data.head() must be run with print to show up its result on the screen.

## Correlation map
'''
print(data.corr()) # quantative information on dataframe.
fig, axe = plt.subplots(figsize=(18, 18))
sns.heatmap(data.corr(), annot=True, linewidths=1, fmt='.2f', ax=axe)
plt.show()
'''

print(data.columns)

## < Introduction to Python >
## Matplotlib
## 1. Line Plot
'''
data.Speed.plot(kind="line", color='g', label="Speed", linewidth=1, alpha=.5, grid=True, linestyle=':')
data.Defense.plot(color='r', label='Defense', linewidth=1, alpha=.5, grid=True, linestyle='-.')
plt.legend(loc='upper right')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot on Speed & Defense")
plt.show()
'''

## 2. Scatter plot
'''
data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
# Scatter plot to show the correlation between Attack and Defense.
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack Defense Scatter Plot : Showing its correlation")
plt.show()
'''

## 3. Histogram
## bins = number of bar in figure
'''
data.Speed.plot(kind="hist", bins=50, figsize=(12,12))
plt.show()
'''

## Pandas
series = data['Defense'] # Return the 'Defense' of data as Series.
data_frame = data[['Defense']] # Return the 'Defense' of data as Data Frame.
print("series type : ", type(series), "\n data_frame type : ", type(data_frame))

# 1 - Filtering Pandas data frame
x = data['Defense']>200 # (비교연산자를 맥였기 때문에 Boolean 형의) Series타입으로 리턴된다.
                        # 만약 데이터 프레임객체로 뭔가 반환하고 싶다면 data[['Defense']]라고 해야겠지
# print(x)
print("data[x] = ") ## data[data['Defense']>200] 와 같다.
print(data[x]) # data란 data frame에다가 x라는 (boolean) series를 맥여서 True에 해당하는 값(행)들만
               # print한다. ;; 리턴 : Data Frame(data) -> Data Frame(data[x])

# 2 - Filtering Pandas with np.logical_and  ***
# np.logical_and 를 써서 두 가지 조건에 둘다 해당하는 녀석들만 추출할 것이다.
# data[np.logical_and(#조건1, #조건2)]
print(data[np.logical_and(data['Defense']>200, data['Attack']>100)])

# 3 - np.logical_and 를 안쓰고 & 라는 빌트인 연산자를 써도 된다.
print(data[(data['Defense']>200) & (data['Attack']>100)])

## Dictionary
# we can use for loop to achieve 'key and value' of dictionary.
dictionary = {}
dictionary['spain'] = 'madrid' # dictionary의 key는 immutable하다. 즉 key는 수정이나 삭제 불가능하다.
                               # value는 수정가능(mutable)
dictionary['france'] = 'paris'
print("dictionary.items() : ", dictionary.items())
# dict_items([('spain', 'madrid'), ('france', 'paris')])
for key, value in dictionary.items(): # dictionary.items
    print(key, " : ", value)
print("")

# For pandas we can achieve index and value
print("data[['Attack']][0:2] = ")
print(data[['Attack']][0:2]) # [0:n] => 0번째 행 부터 n-1번째 행들의 정보를 추출
for idx, value in data[['Attack']][0:5].iterrows(): # dataframe객체의 iterrows는 행들을
                                                    # 순차적으로 인덱스를 매기면서 값을 리턴하는 generator이다.
    print(idx, " : ", value)

def tuple_ex():
    """ return defined t tuple """
    t = (1,2,3)
    return t

a,b,_ = tuple_ex() # unpack tuple into several variables. can be used blank variable(_)
print(a,b)

## Scope
# 파이썬이 Scope를 참조하는 순서는
# Local Scope -> Enclosing Scope -> Global Scope -> Built in Scope
# 위 순서대로 참조한다. 이 때 local scope는 가장 작은 단위의 함수또는 클래스 내의 범위이다.
# enclosing scope는 함수를 감싸고 있는 클래스나 함수 내의 범위다.
# Global scope는 말그대로 전역범위
# Built in Scope 는 파이썬 프로그램에 내장된 범위
# 파이썬에 내장된 빌트인 함수 또는 클래스, 변수들을 보고 싶으면 <builtins>를 import하면 된다.
import builtins
print(dir()) # dir() 이 역시 파이썬 빌트인 함수인데, 현재 선언한 scope에서의 name list들을 보여준다.
print(dir(builtins)) # builtins 내에 선언되어있는 name list를 보여준다.
print(dir(np)) # eg. numpy에 선언되어 있는 name list들.

print(len(dir(builtins))) # 파이썬에 내장되어있는 name은 몇개나 될까 -> 153개

## Default and Flexible Arguments
# 1. Default argument ex.
# def f(a, b=1): -> b=1 is default argument

# 2. Flexible argument ex1.
# def f(*args):  -> *args can be one or more

# 3. Flexible argument ex2.
# def f(**kwargs): -> **kwargs is a "dictionary"

def f(*args):
    print(args) # tuple로 받아옴.
    for i in args:
        print(i)
print("f([1,2,3], [4,5,6,7]) = ", end='') # without new line by print(" ", end='')
f([1,2,3], [4,5,6,7]) # return -> ([1,2,3], [4,5,6,7])
# f(1,2,3,4)

def f(**kwargs):
    """ print 'key and value' of dictionary """
    print(kwargs)
    for key, value in kwargs.items(): # dictionary.items() -> return all (key,value) tuples in dictionary.
        print(key, " : ", value)

f(country='spain', capital='madrid', population=123456)
# {'country' : 'spain', 'capital' : 'madrid', 'population' : 123456}

## Lambda Function
# : Faster way of writing function. 정의함수 빠르게 사용하는 방법.
square = lambda x: x**2 # x는 입력변수 -> square는 함수다 이제.
print(square(4))
tot = lambda x,y,z: x+y+z # x,y,z 입력변수 -> tot도 이제 함수다.
print(tot(1,2,3))

## Anonymous Function
# Lambda 함수와 비슷한데, 이 때는 함수를 각기 다른 요소에 모두 동일하게 적용할 수 있게 해준다. (broadcasting 처럼)
number_list = [1,2,3]
y = map(lambda x: x**2, number_list)
# map(func, seq) : seq(list)에 있는 모든 요소들에 func을 다 적용한다.
print(y) # 그냥 map 객체임.
print(list(y)) # map객체는 list화해야지 볼수 있음.

## Iterators
# iterable is an object that can return an iterator.
# iterable : an object with an associated iter() method (eg. list, strings, and dictionaries)
# iterator : produces next value with next() method.
name = 'yungiKwon'
it = iter(name) # By using iter() method, generate its iterator named 'it'.
print(it) # str_iterator 라는 객체(object)이다.
print(next(it)) # print next iteration. 처음 next() method는 시작(즉, next()하면 첫번째 단어(y)가 시작됨)을 알린다.
print(*it) # iterator는 기본적으로 소모되는 것이다. (유지되지않음), 즉, print(*it)는 남은 iteration을 보여준다.

## zip() : zip list.
# 두 개의 리스트 또는 튜플을 element-wise하게 요소끼리 서로 엮음.
# 묶여진 요소들은 튜플화되고, 이 전체 묶음이 추상적인 zip 객체(object)로 반환됨.
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1, list2)
print(z) # <zip object at 0xblahblah>
z_list = list(z)
print(z_list) # [(1,5), (2,6), (3,7), (4,8), (5,9)]

# unzip : 두 개 묶여진 요소들을 떼어버림.
un_zip = zip(*z_list) # *가 핵심임.
print(un_zip) # 이것도 추상적인 zip객체; <zip object at 0xblahblahblah>
un_list1, un_list2 = list(un_zip) # 존나웃긴게 un_zip한 zip객체를 list()하면 tuple들로 묶임.
print(un_list1) # tuple
print(un_list2) # tuple
print(type(un_list2)) # <class 'tuple'>


## LIST COMPREHENSION ***
# One of the most important topic of this kernel
# List Comprehension is used for data analysis very often.
num1 = [1,2,3]
num2 = [i+1 for i in num1] # LIST COMPREHENSION ( i+1 : list comprehension syntax(구문론; 신택스;))
print(num2)

# Conditionals on iterable : 반복문에 조건문 적용한 COMPREHENSION
num1 = [5, 10, 15, 9, 6]
num2 = [i if i==10 else i-5 if i<7 else i+100 for i in num1]
# 짚고 넘어갈 점! : 보통 conditional list comprehension은 [i for i in range(10) if >= 5]
# 와 같은 형태이다. (if 문이 뒤에 위치)
# 그러나 else문도 같이 사용한다면, 구문순서가 달라진다.
# -> [i if i >= 5 else 'None' for i in range(10))] 즉 for와 if의 순서가 바뀐다.
# else가 없는 기본적인 if - list comprehension은 [for i in range if ] 임을 기억하자!
# !!! 와 개같은 거
# [ i if i==10 else i-5 if i<7 else i+100 for i in num1]의 의미는.
# if 조건1_효과 else 조건2_'효과'' if 조건2 else 조건1_우회 라고 보면 된다.
# num1의 5기준 ) 1. 5가 10이랑 같은지 / 2. 5가 7보다 작은지 작다면 "else 조건2_효과" 적용하고 끝
#              / 3. 조건2에 부합하지 않으면 "else 조건1_우회" 를 적용하고 끝.
print(num2)

## lets classify pokemons whether they have high or low speed.
# Our threshold is average speed.
print(data.head())
print(data.columns)
print("data.Speed = \n", data.Speed, "\n type(data.Speed) = ", type(data.Speed))
threshold = sum(data.Speed) / len(data.Speed) # speed average
data['speed_level'] = ["high" if i>threshold else "low" for i in data.Speed] # Series 추가된거
print(data.columns) # speed_level이라는 시리즈가 하나 더 생김. (시리즈 만들기 쉽네) 
print(data['speed_level'], "\n data['speed_level의 타입은 =>", type(data['speed_level'])) # Series다.
print(data.loc[:10, ["speed_level", "Speed"]]) # we will learn df.loc more detailed later.
# df.loc[] (*소괄호()가 아니다. loc은 대괄호[]임에 유의하자 )
# df.loc[]은 간단히 말하면 '조회'를 해주는 메소드다.
