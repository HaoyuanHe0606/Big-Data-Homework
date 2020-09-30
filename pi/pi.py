#!/usr/bin/env python
# coding: utf-8

# In[1]:


def TaylorPi(k):
    sum,odd = 0,True
    for i in range(1,k):
        sum += 1/(2*i-1) if odd==True else -1/(2*i-1)
        odd = not odd
    print("Taylor PI:",sum*4)


# In[2]:


TaylorPi(1000000)


# In[ ]:





# In[ ]:




