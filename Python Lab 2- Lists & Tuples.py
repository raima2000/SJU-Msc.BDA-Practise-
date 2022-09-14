#!/usr/bin/env python
# coding: utf-8

# In[1]:


# LISTS

list1=[10,20,30]
list2=[1,2,3,'hello world',2.3]


# In[2]:



list2


# In[3]:


list1


# In[4]:


list1.extend(list2)
list1


# In[ ]:





# In[5]:


list1.append(11) # adding elements to the end of list
list1


# In[6]:


list1.append(11,13) # not possible
list1


# In[7]:


list1.insert(3,44) # adding elements to a specific position in a list (first value is index and sec is the value to be entered)
list1


# In[10]:


list2.clear() # will clear all the entries
list2


# In[11]:


list1.count(10) # count the occurance of the element mentioned 


# In[12]:


list1.pop() # will remove the last element
list1


# In[14]:


list1.pop(4) # will remove the specific element


# In[15]:


list1


# In[16]:


list1.remove(20)
list1


# In[19]:


list3=[11,12,13,4,2]
list3


# In[20]:


list3.sort() # sort ascending
list3


# In[21]:


list3.sort(reverse=True) # sort descending
list3


# In[22]:


list4=['a','d','g','b']
list4


# In[24]:


list4.sort()
list4


# In[37]:


dairy=['paneer','milk','cheese','butter']
dairy


# In[27]:


dairy1=[]               # list comprehension (to get the products that contain letter 'e' in the name)
for i in dairy:
    if 'e' in i:
        dairy1.append(i)
print(dairy1)        


# In[28]:


dairy1=dairy.copy()    # to copy contents of 1 list to a new list
print(dairy1)


# In[29]:


dairy1=list(dairy) # if you want outcome in list   
print(dairy1)


# In[30]:


# TUPLES


# In[32]:


tuple1=(1,4,7,2,1)
tuple1


# In[33]:


tuple1.count(1)


# In[34]:


tuple1.index(4)    # prints the index of the value


# In[40]:


# creating tuple from list

dairy2=tuple(dairy1)
print(dairy2)
    


# In[43]:


dairy3=list(dairy2)   # to edit elements in a tuple we need to first convert it into list as direct changes arent possible
print(dairy3)
dairy3[2]='ghee'# the changes
dairy3


# In[44]:


dairy2=tuple(dairy3)  # after making the changes convert it back into tuple
print(dairy2)


# In[ ]:




