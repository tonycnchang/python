import pandas as pd


res = pd.merge(df1,df2,on='key',how='outer',indicator='True')
