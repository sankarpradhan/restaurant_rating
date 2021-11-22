import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as py
import seaborn as sns

import matplotlib.ticker as mtick
plt.style.use('fivethirtyeight')
# https://matplotlib.org/stable/gallery/style_sheets/fivethirtyeight.html
# https://towardsdatascience.com/a-beginners-guide-to-plotting-fivethrityeight-like-visualizations-5b63d3f3ddd0
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import  ExtraTreesRegressor
from sklearn.ensemble import  RandomForestRegressor

from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')
import os


a= 50
b = 20
print (a+b)
import pandas as pd
df=pd.read_csv('zomato_df.csv')
print (df)
