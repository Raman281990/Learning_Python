# In order to perform data analysis and manipulation we need pandas
# pandas are build on top of Numpy and Matplotlib


# Series is a one dimensional array holding one type of data
import pandas as pd

list_of_names =['Raman','Gagan','Navdeep']
list_of_indexes = [0,1,2]
series = pd.Series(list_of_names,list_of_indexes)
print(series)

# creating series using dictionaries
dictat = dict()


