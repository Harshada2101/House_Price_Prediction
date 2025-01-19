#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[37]:


train = pd.read_csv('../../datasets/house-prices/train.csv')
test = pd.read_csv('../../datasets/house-prices/test.csv')


# In[57]:


train['MSZoning'].value_counts()


# In[38]:


train.head()


# In[39]:


test.shape


# In[40]:


test.head()


# In[26]:


train.isnull().sum()


# In[42]:


test.isnull().sum()


# In[22]:


sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()


# In[23]:


train.shape


# In[30]:


train.info()


# In[31]:


train['LotFrontage']=train['LotFrontage'].fillna(train['LotFrontage'].mean())


# In[43]:


test['LotFrontage']=test['LotFrontage'].fillna(test['LotFrontage'].mean())


# In[44]:


test['MSZoning']=test['MSZoning'].fillna(test['MSZoning'].mode()[0])


# In[45]:


test.shape


# In[46]:


test.drop(['Alley'],axis=1,inplace=True)


# In[47]:


test.shape


# In[29]:


train['BsmtCond']=train['BsmtCond'].fillna(train['BsmtCond'].mode()[0])
train['BsmtQual']=train['BsmtQual'].fillna(train['BsmtQual'].mode()[0])


# In[34]:


train['FireplaceQu']=train['FireplaceQu'].fillna(train['FireplaceQu'].mode()[0])
train['GarageType']=train['GarageType'].fillna(train['GarageType'].mode()[0])


# In[55]:


train['GarageFinish']=train['GarageFinish'].fillna(train['GarageFinish'].mode()[0])
train['GarageQual']=train['GarageQual'].fillna(train['GarageQual'].mode()[0])
train['GarageCond']=train['GarageCond'].fillna(train['GarageCond'].mode()[0])


# In[56]:


train.shape


# In[59]:


train.drop(['Id'],axis=1,inplace=True)


# In[60]:


train.isnull().sum()


# In[61]:


train['MasVnrType']=train['MasVnrType'].fillna(train['MasVnrType'].mode()[0])
train['MasVnrArea']=train['MasVnrArea'].fillna(train['MasVnrArea'].mode()[0])


# In[62]:


sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='coolwarm')
plt.show()


# In[ ]:


train['BsmtExposure']=train['BsmtExposure'].fillna(train['BsmtExposure'].mode()[0])


# In[63]:


sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='YlGnBu')
plt.show()


# In[64]:


train['BsmtFinType2']=train['BsmtFinType2'].fillna(train['BsmtFinType2'].mode()[0])


# In[65]:


train.dropna(inplace=True)


# In[66]:


train.shape


# In[67]:


train.head()


# In[72]:


columns = ['MSZoning','Street','Lotshape','Landcontour','Utilities','LotConfig','LandSlope','Neighborhood',
          'Condition2','Bldgtype','Condition1','HouseStyle','Saletype','SaleCondition','ExterCond','ExterQual'
          'Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','RoofStyle','RoofMatl',
           'Exterior1st','Exterior2nd','MasVnrType','Heating','HeatingQC','CentralAir','Electrical','KitchenQual'
          'Functional','FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive']


# In[73]:


len(columns)


# In[75]:


def category_onehot_multcols(multcolumns):
    df_final=final_df
    i=0
    for fields in multcolumns:
        print(fields)
        df1=pd.getdummies(final_df[fields],drop_first=True)
        final_df.drop([fields],axis=1,inplace=True)
        if i==0:
            df_final=df1.copy()
        else:
            df_final=pd.concat([df_final,df1],axis=1)
        i=i+1
    df_final=pd.concat([final_df,df_final],axis=1)
    return df_final


# In[77]:


main_df=train.copy()


# In[85]:


final_df = test.to_csv('formulatedtest.csv',index=False)


# In[ ]:




