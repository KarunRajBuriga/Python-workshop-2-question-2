#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 


# In[ ]:


df=pd.read_csv('Documents\\sales_1.csv')


# In[ ]:


df


# In[ ]:


df1=pd.read_csv('Documents\\sales_2.csv')


# In[ ]:


df1


# In[ ]:


df2=pd.concat([df,df1],axis=0)


# In[ ]:


df2


# In[ ]:


df3=df2.melt(id_vars=['PRODUCT_TYPE'],var_name='SOLD_DATE',value_name='QTY_SOLD')
df3


# In[ ]:


df3.to_csv('C:\\Users\\KBuriga\\final.csv')

