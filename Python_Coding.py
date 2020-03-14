#!/usr/bin/env python
# coding: utf-8

# In[3]:


for i in range(10):
    if(i%3)==0:
        print(i)
    


# In[4]:


#new_list = [expression(i) for i in old_list if filter(i)]

output = [print(i) for i in range(10) if i%3 ==0]


# In[2]:


output = [print(i,j,k) for i in range(2) for j in range(2) for k in range(2) if i+j+k <100]


# In[ ]:




