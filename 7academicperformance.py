# -*- coding: utf-8 -*-
"""7AcademicPerformance.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mk5TfA0OC5N_2RzfADzfDQ3zapVo6GQU

<pre>
1. Load the Academic Performance dataset in data frame object.
2. Check null values in the dataset.
3. Check missing values in dataset and replace the null values with standard null value NaN
4. Replace the missing value of Math Score with Mean Value
5. Replace the missing value of Reading Score with standard deviation
6. Replace the missing value of place with common value "Nashik"
</pre>
"""

import pandas as pd

df = pd.read_csv('AcademicPerformance.csv', na_values=['na', 'Na'])
df

#Check for Null values in dataset
df.isnull()

df.isnull().sum()

df['math score'].mean()

#repalce nan value of Math_Score with mean value
df['math score'].fillna(value = df['math score'].mean(), inplace = True)

df['math score']

#  Replace the missing value of Reading Score with standard deviation
df['reading score'].fillna(value = df['reading score'].std(), inplace = True)

df['reading score']

# Replace the missing value of place with common value "Nashik"
df['Region'].fillna(value = 'Nashik', inplace = True)

df