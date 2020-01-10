import pandas as pd
import numpy as np

#series1 = pd.Series([1,5,9,7,np.nan,23,11])

dates = pd.date_range('20160803',periods=3)

dataframe = pd.DataFrame(np.random.randn(3,4),index=dates,columns=['a','b','c','d'])

#df = pd.DataFrame(np.arange(12).reshape(3,4))

#df1 = pd.DataFrame({'a':1,'b':'q','c':['a','b','c']})

#print(df1.dtypes)

#print(df1.index,df1.columns)

#print(df1.values)

#print(df1.describe())

#print(df1.T)

#print(df1.sort_index(axis=0,ascending=False))  #排序，ascending=False倒序

#print(df1.sort_values(by='c',ascending=False)) #按内容排序
"""
筛选
#print(dataframe)
#print(dataframe['a'])
#print(dataframe.a)
#print(dataframe[0:2],dataframe['20160803':'20160805'])

#print(dataframe.loc['20160804'])           #select by label
#print(dataframe.loc['20160804','a':'c'])

#print(dataframe.iloc[1:3,2:3])            #select by position

#print(dataframe.ix[1:3,['a','c']])          #mixed select

print(dataframe)
print(dataframe.a>0)
print(dataframe[dataframe.a>0])      #boolean index :True False
"""
