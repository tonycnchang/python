import pandas as pd
import numpy as np

#concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,index=['1','2','3'],columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
df4 = pd.DataFrame(np.ones((3,4))*2,index=['2','3','4'],columns=['B','C','D','E'])

#res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)


#join,['inner','outer']
#res = pd.concat([df1,df4],join='inner')

#join_axes
#res = pd.concat([df1,df4],axis=1,join_axes=[df4.index])


#append
#res = df1.append(df4,ignore_index=True)
#res = df1.append([df2,df4],ignore_index=True)
s1 = pd.Series([1,2,3,4],index=['A','B','C','D'])
res = df1.append(s1,ignore_index=True)
print(res)

