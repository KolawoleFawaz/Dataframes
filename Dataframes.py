# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

df = pd.DataFrame(exam_data,columns=['name','score','attempts','qualify'])
df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#printing the first three rows using head method
print(df.head(3))

#deleting rows with nan values
df1 = df.drop(['d','h'],axis='index')

#extracting name and score from the dataframe
print(df1.iloc[:,1])
print(df1.iloc[:,3])
print(df1)

#program to append new row K to the Dataframe
k = {'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}
df2 = df1.append(k,ignore_index=True)
df2.index = ['a', 'b', 'c','e', 'f', 'g','i', 'j','k']
print(df2)

#program to delete the 'attempts' column from the DataFrame.
df3 = df2.drop('attempts',axis='columns')
print(df3)
 
 #new column success
Success = [1,0,1,0,1,1,0,1,1]
df3["Success"] = Success
print(df3)

#exporting final dataframe to csv file
my_data = df3.to_csv('my_data')






