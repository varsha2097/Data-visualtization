#!/usr/bin/env python
# coding: utf-8

# In[43]:


#milk production
import pandas as pd
df = pd.read_csv("milk_production.csv")
df.head()
milk=df
milk


# In[44]:


df.head()
df.fillna(0)


# In[45]:


#first
import numpy as np

sum=df["Cow Milk-2013-14"]+df["Boffalo Milk-2013-14"]+df["Goat Milk-2013-14"]
print(sum.max())
a=np.where(sum==sum.max())
state=df.iloc[a]
state["State/ UT Name"]


# In[46]:


#second
df["y2011"] =(df["Cow Milk-2010-11"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]).sort_values(ascending=False)
df["y2012"]= (df["Cow Milk-2011-12"] + df["Boffalo Milk-2011-12"] + df["Goat Milk-2011-12"]).sort_values(ascending=False)
df["y2014"]= (df["Cow Milk-2013-14"] + df["Boffalo Milk-2013-14"] + df["Goat Milk-2013-14"]).sort_values(ascending=False)
df["y2015"]= (df["Cow Milk-2014-15"] + df["Boffalo Milk-2014-15"] + df["Goat Milk-2014-15"]).sort_values(ascending=False)
print(df.sort_values('y2011',ascending=False)["State/ UT Name"].head())
#print(df.sort_values('y2012',ascending=False)["State/ UT Name"].head())
#print(df.sort_values('y2014',ascending=False)["State/ UT Name"].head())
#print(df.sort_values('y2015',ascending=False)["State/ UT Name"].head())


# In[50]:


#third
df=milk
df=df1.fillna(0)
df1["2010"]=df1.iloc[:,3]+df1.iloc[:,8]+df1.iloc[:,13]
df1["2011"]=df1.iloc[:,4]+df1.iloc[:,9]+df1.iloc[:,14]
df1["2013"]=df1.iloc[:,5]+df1.iloc[:,10]+df1.iloc[:,15]
df1["2014"]=df1.iloc[:,6]+df1.iloc[:,11]+df1.iloc[:,16]
df1["2015"]=df1.iloc[:,7]+df1.iloc[:,12]+df1.iloc[:,17]

df1[(df1["2015"]>df1["2014"])&(df1["2014"]>df1["2013"])&(df1["2013"]>df1["2011"])]
df1.head()


# In[54]:


#fourth
df["y2011"] =(df["Cow Milk-2010-11"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]).sort_values(ascending=False)
df["y2012"]= (df["Cow Milk-2011-12"] + df["Boffalo Milk-2011-12"] + df["Goat Milk-2011-12"]).sort_values(ascending=False)
df["y2014"]= (df["Cow Milk-2013-14"] + df["Boffalo Milk-2013-14"] + df["Goat Milk-2013-14"]).sort_values(ascending=False)
df["y2015"]= (df["Cow Milk-2014-15"] + df["Boffalo Milk-2014-15"] + df["Goat Milk-2014-15"]).sort_values(ascending=False)
df["y2016"]= (df["Cow Milk-2015-16"] + df["Boffalo Milk-2015-16"] + df["Goat Milk-2015-16"]).sort_values(ascending=False)
df[df["y2016"].ge(df["y2015"]) & df["y2015"].ge(df["y2014"])].head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


df["cow_allyear"]=df["Cow Milk-2010-11"]+df["Cow Milk-2011-12"]+df["Cow Milk-2013-14"]+df["Cow Milk-2014-15"]+df["Cow Milk-2015-16"]
df[df["cow_allyear"].mean() and df["State/ UT Name"]=="Uttar Pradesh"]


# In[55]:


#oil reserve

import pandas as pd
df = pd.read_csv("oil_reserves.csv")
df.head()


# In[56]:


#first
import numpy as np

sum=df["2014"]+df["2015"]+df["2016"]
print(sum.max())
a=np.where(sum==sum.max())
reg=df.iloc[a]
reg["Region"]


# In[123]:


#second
df['2010'],df['2011'],df['2012'],df['2013'],df['2014'],df['2015'],df['2016'].plot(kind="bar", figsize=(15,7), color="#61d199")
#oil['2011'].plot(kind = "bar",flagsize=(15,7),color ="#61d199")
plt.show()


# In[107]:


#third
df["North America"]=df["2010"]+df["2011"]+df["2012"]+df["2013"]+df["2014"]+df["2015"]+df["2016"]
df.sort_values(by="North America",ascending=False).iloc[:3,:]


# In[116]:


df["S. & Cent. America"]=df["2010"]+df["2011"]+df["2012"]+df["2013"]+df["2014"]+df["2015"]+df["2016"]
df.sort_values(by="S. & Cent. America",ascending=False).iloc[4:7,:]


# In[118]:


df["Europe & Eurasia"]=df["2010"]+df["2011"]+df["2012"]+df["2013"]+df["2014"]+df["2015"]+df["2016"]
df.sort_values(by="Europe & Eurasia",ascending=False).iloc[7:16,:]
df.max()


# In[121]:


#fourth
import matplotlib.pyplot as plt

df=pd.read_csv("oil_reserves.csv")
labels=df.iloc[:]
#labels = ["2010","2011","2012","2013","2015","2016"]
sizes = [38.4, 40.6, 20.7, 10.3]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
patches, texts = plt.pie(sizes, explode, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[124]:


plt.scatter(df['2010'],df['2011'],color ='blue')
plt.show()


# In[125]:


plt.scatter(df['2012'],df['2013'],color ='blue')
plt.show()


# In[126]:


plt.scatter(df['2014'],df['2015'],color ='blue')
plt.show()


# In[ ]:




