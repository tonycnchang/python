import pandas as pd
import numpy as np

dates = pd.date_range('20160804',periods=6)
labels = ['A','B','C','D','E']

df1 = pd.DataFrame(np.random.random_integers(1,31,size=30).reshape((6,5)),index=dates,columns=labels)

print(df1)

df1.iloc[2,2]=100
df1.loc['20160804','B']=101
df1.B[df1.A>5]=0
df1['F']=np.nan
df1['g']=pd.Series([2,2,2,3,3,3],index=dates)

print(df1)


#print(df1.dropna(axis=0,how='all'))
#print(df1.dropna(axis=0,how='any'))
#print(df1.fillna(0))

#print(df1.isnull())

print(np.any(df1.isnull())==True)
