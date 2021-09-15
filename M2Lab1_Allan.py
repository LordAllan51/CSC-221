# coding: utf-8
import pandas as pd
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision', 2)
titanic.head()
titanic.tail()
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']
titanic.head()
titanic.describe()
(titanic.survived == 'yes').describe()
get_ipython().run_line_magic('matplotlib', '')
histogram = titanic.hist()
