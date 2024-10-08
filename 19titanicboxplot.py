# -*- coding: utf-8 -*-
"""19titanicBoxPlot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p4A7N3dkSPdSCDZ0UuzW_jmRzgobj9LA

1. Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for distribution of age with respect to each gender along with the
information about whether they survived or not. (Column names : 'sex' and 'age')
2. Write observations on the inference from the above statistics.
"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()

df.isna().sum()

sns.boxplot(x ='sex', y = 'age', hue = 'survived', data = df)

