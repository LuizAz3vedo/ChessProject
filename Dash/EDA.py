# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# data processing
df = pd.read_csv("Df\games.csv")

null_values_per_column = df.isnull().sum()

# check if there are any null values in the entire DataFrame
total_null_values = df.isnull().sum().sum()

# print
print('values null:', null_values_per_column)
print('total values null:', total_null_values)

# checking if you have duplicate columns
duplicate_columns = df.columns[df.columns.duplicated()]
print('duplicate columns:', duplicate_columns)

# data types
data_types = df.dtypes
print('data types:', data_types)

df.info()

df.describe()

df.nunique()

# visualize the distribution of numerical variables
sns.pairplot(df)
plt.show()

# Visualize the correlation between numerical variables
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Visualize the distribution of a categorical variable
sns.countplot(x='victory_status', data=df)
plt.show()

# Visualize the distribution of a categorical variable
sns.countplot(x='rated', data=df)
plt.show()

# handling of the opening_name column
df['first_name_opening'] = df['opening_name'].str.split(':').str[0]
print(df['first_name_opening'])

# counting the occurrences and taking the 3 highest values
c_opening = Counter(df['first_name_opening'])
top_3_openings = c_opening.most_common(3)
print(top_3_openings)

# Visualize the distribution of a categorical variable
sns.countplot(x='first_name_opening', data=df, order=[item[0] for item in top_3_openings])
plt.show()