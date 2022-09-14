#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= 21
b=45


# In[2]:


c=a+b


# In[3]:


print(c)


# In[4]:


print(b-a)


# In[5]:


print(a*b)


# In[7]:


x=10 # even if we dont mention the datatype, its the responsibility of python interpreter to identify the datatype
y=5
print(x/y)


# In[8]:


print(x//y) #returns integer value


# In[9]:


x=10 # should give the variables and print statement in the same cell
y=5
print("The added value is",x+y)
print("The subtracted value is",x-y)
print("The multiplied value is",x*y)
print("The divided value is",x/y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[11]:


#FOR LOOP
for i in range(1,11): # write a program in for loop to print 1-10 in order
    print(i)


# In[13]:


for i in range(0,111,5): # write a program in for loop to print no. 0-100 with jump seq of 5
    print(i)


# In[14]:


a= 10   # we get error cus no addition & subtraction bw int & str under python
b="Simple"
a+b
a-b


# In[16]:


a="Life" #
b="simple"
a+b


# In[17]:


a*b


# In[18]:


a= 10   
b="Simple"
a*b


# In[19]:


L1=[2,5,8,4,7,6,3]
for i in L1:
    print(i)


# In[20]:


L2=["sing",2,5.9,"dance"]
for i in L2:
    print(i)
    


# In[21]:


k=8 # no of rows
for i in range(1,9): # for printing no from 0-8
    for j in range(0,k): 
        print(end=" ")
    k=k-1                   #to reduce the spacing and start from one space less in the succeeding line
    for j in range(1,i+1):
        print(j,"",end='')
    print("\r") # going to the next line(\r)   
     


# In[22]:


k=8 # no of rows
for i in range(1,9): # for printing no from 0-8
    for j in range(0,k): 
        print(end=" ")
    k=k-1                   #
    for j in range(,i+1):
        print(j,"",end='')
    print("\r") # going to the next line(\r) 


# In[ ]:




