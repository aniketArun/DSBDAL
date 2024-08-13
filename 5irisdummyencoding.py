# -*- coding: utf-8 -*-
"""5IrisDummyEncoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oybO3D6q5aT86tRieuOYKyrjF9sK9oDr

<pre>
1. Locate open Iris dataset from the URL csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
2. Perform the Dummy Variable Encoding , by considering Species as target variable
</pre>
"""

import pandas as pd

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(csv_url, names = columns)

df.head()

df.tail()

pd.get_dummies(df, columns=['species'])

pd.get_dummies(df['species']).head().astype(int)

pd.get_dummies(df)