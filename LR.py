#!/usr/bin/env python
# coding: utf-8

# In[25]:


from sklearn.linear_model import  LinearRegression 
import matplotlib.pyplot as plt
import seaborn as sb 


a=[[1],[2],[3],[5],[3],[5],[8]]
b=[5,3,8,0,3,5,7]

lr=LinearRegression()
lr.fit(a,b)
print(lr.score(a,b))

print(lr.predict([[4]]))
plt.plot(a,lr.predict(a),color='red')


plt.scatter(a,b)
plt.show


# In[28]:


arr=a
a="helo","world"
a=[1,2,3,4]
print(a)
print(type (a))


# In[ ]:




