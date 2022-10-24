#!/usr/bin/env python
# coding: utf-8

# DICTIONARIES

# In[1]:


dict1={'Brand':'Apple','Industry':'Gadgets','Year':1880}
print(dict1)


# In[2]:


dict2={}
dict2


# In[3]:


type(dict2)


# In[4]:


dict3=dict([(5,'happy'),(6,'world')])        # converting list to dictionary
print(dict3)


# In[6]:


dict4=dict(((5,'happy'),(6,'world')))       # converting tuple to dictionary
print(dict4)


# In[5]:


type(dict3)


# In[9]:


countries={
    ('India','Delhi'),
    ('UAE','AbuDhabi'),
    ('Australia','Melbourne'),
    ('Andaman','Kavarati'),
    ('Afganistan','Kabul')}
country_cap=dict(countries)
print(country_cap)


# Accessing Dictionaries

# 1) Add value

# In[14]:


country_cap['Andaman']='Island'
country_cap


# 2) Casting values

# In[15]:


print(country_cap['India'])


# Deleting Dictionaries

# 1)Deleting single item

# In[16]:


del country_cap['UAE']
print(country_cap)


# 2) Deleting Entire content

# In[17]:


country_cap.clear()
print(country_cap)


# 3) Deleting both data & structure

# In[18]:


del country_cap


# In[19]:


country_cap


# In[21]:


countries={
    ('India','Delhi'),
    ('UAE','AbuDhabi'),
    ('Australia','Melbourne'),
    ('Andaman','Kavarati'),
    ('Afganistan','Kabul')}
country_cap=dict(countries)
print(country_cap)


# In[22]:


type(country_cap)


# In[23]:


print(len(country_cap))


# In[25]:


proj_details={
    'std_name':'Bloom',
    'std_no':'222bda90',
    'proj_comp':True,
    'year':2022,
    'sub':['maths','eng','stat']
}
print(proj_details)


# In[26]:


x=proj_details.get("std_name")
x


# In[27]:


x=proj_details.keys() #  method will return a list of all the keys in the dictionary.
x


# In[28]:


x=proj_details.values()   # method will return a list of all the values in the dictionary.
x


# In[ ]:




