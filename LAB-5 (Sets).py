#!/usr/bin/env python
# coding: utf-8

# # SETS

# In[1]:


set1={20,40,"weather"}
set1


# In[2]:


set1.add(100) # can use add statement in sets to add elements unlike list/tuple
set1


# In[3]:


set2=set((10,20,30,[1,'a','b'])) # will get error
set2


# In[13]:


set3=set((10,20,30,(1,'a','b')))
set3


# In[14]:


set3.update('t','r','x')   # can only update with characters
set3


# In[15]:


set3.remove(20)
set3


# # Q. WAPP to implement list along with some list methods

# In[12]:


list1=[1,2,3,4,5]
print(list1)
list1.append(20)
list1.insert(2,30)
list1.pop(4)
print(list1)


    


# # Q. WAPP to convert the given list of multiple integers into single integers

# In[11]:


list_2=[10,20,30,40,50]
for i in list_2:
    print(i,end="")


# # Q. WAPP to calculate product multiplying all the no given in tuple

# In[ ]:


x=
tuple1=(20,30,40,50,60)

