import pandas as pd
import matplotlib.pyplot as plt
# Jupyter magic matplotlib inline so that plots are displayed inline.
% matplotlib inline
recent_grads = pd.read_csv('recent-grads.csv')

# Return first row, head & tail to become familiar with data structure 
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())
# Drop rows with missing values
recent_grads = recent_grads.dropna()

# Now Generate scatter plots to explore the following relations:
# Sample_size and Median
recent_grads.plot(x='Sample_size', y='Median', kind='scatter')

# Sample_size and Unemployment_rate
recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')

# Full_time and Median
recent_grads.plot(x='Full_time', y='Median', kind='scatter')

# ShareWomen and Unemployment_rate
recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')

# Men and Median
recent_grads.plot(x='Men', y='Median', kind='scatter')

# Women and Median
recent_grads.plot(x='Women', y='Median', kind='scatter')

# PANADAS, HISTOGRAMS
# Generating histograms to explore the distributions of the following columns:
cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
fig = plt.figure(figsize=(5,12))
for r in range(1,5):
    ax = fig.add_subplot(4,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)
    
cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(4,8):
    ax = fig.add_subplot(4,1,r-3)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)

##  PANDAS, SCATTER MATRIX PLOT    
# Importing scatter matrix to visualize both scatter plots and histograms into one grid of plots
# Creating a 2 by 2 scatter matrix plot using the Sample_size and Median columns.
from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))

# Creating a 3 by 3 scatter matrix plot using the Sample_size, Median, and Unemployment_rate columns.
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))

## PANDAS, BAR PLOTS
# Use bar plots to compare the percentages of women (ShareWomen) from
# the first ten rows and last ten rows of the recent_grads dataframe.
recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)

# Use bar plots to compare the unemployment rate (Unemployment_rate) from 
# the first ten rows and last ten rows of the recent_grads dataframe.
recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)


