import numpy as np
#numpy

#Q1: Given a 2D NumPy array A of shape (5, 5), subtract the mean of each row from every element in that row without using a loop.

a=np.array([(1,2,3,4,5),(2,3,4,5,6),(3,4,5,6,7),(4,5,6,7,8),(5,6,7,8,9)])
b=a.mean(axis=1)
b=np.resize(b,(5,1))
a=a-b
print(a)

# Q2:You have a NumPy array of integers from 1 to 1000. Return a new array containing only the numbers that are divisible by both 3 and 7 but not by 5

a=np.arange(0,1000,1)
b=np.zeros(1000, dtype=int)
j=0
for i in range(1000):
    if(a[i]%3==0 and a[i]%7==0 and a[i]%5!=0 ):
        b[j]+=a[i]
        j+=1
b=np.resize(b,j)
print(b)

# Q3: Create an 8x8 NumPy array with a chessboard pattern (alternating 0s and 1s), where the top-left element is 0.

a=np.zeros((8,8),dtype=int)
count=0
for i in range(8):
    for j in range(8):
        if(j%2==0 and i%2!=0):
           a[j][i]=1
        if(j%2!=0 and i%2==0):
           a[j][i]=1
print(a)

#Pandas

# Q1: Given a DataFrame df with columns: ["department", "employee", "salary"], normalize the salary within each department (i.e., for each department, subtract the mean and divide by the std of that department).

import pandas as pd
#df=pd.DataFrame(
#    {'department':['CS','IT','AIML','EXTC','MECH'],
#    'employee':['A','B','C','D','E'],
#     'Salary':[20000,22000,25000,18000,15000]
#    })
#b=df.mean()
#c=df.std()
#
#def fx(a):
#    return (a-b)/c
      
#df['salary_norm'] = df['Salary'].apply(fx)

#print(df)

#Q2: Given a DataFrame with columns ["timestamp", "user_id", "action"], where timestamp is in string format, find the average number of actions per user per day.

#DOUBT

#Q3: You have a DataFrame with columns: ["user_id", "product", "price", "quantity", "date"]. Calculate the total amount spent by each user on "Laptop" purchases only, and return the result as a new DataFrame with columns: ["user_id", "total_spent_on_laptops"].

