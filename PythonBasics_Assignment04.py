#!/usr/bin/env python
# coding: utf-8

# ## 1. What exactly is [ ]?

# Ans: This [ ] is a emplty list,example like a =[ ]

# ## 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[1]:


#  change the value in index 3 by hello
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
spam


# ### Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# In[2]:


spam=['a', 'b', 'c', 'd']


# In[3]:


spam


# ## 3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[4]:


spam[int(int('3' * 2) / 11)]


# ## 4. What is the value of spam[-1]?

# In[6]:


spam[-1]


# ## 5. What is the value of spam[:2]?

# In[7]:


spam[:2]


# ### Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

# In[8]:


bacon=[3.14, 'cat', 11, 'cat', True]


# In[9]:


bacon


# ## 6. What is the value of bacon.index('cat')?

# In[10]:


# it returns the index of first occurrence of 'cat'
bacon.index('cat')


# ## 7. How does bacon.append(99) change the look of the list value in bacon?

# In[11]:


bacon.append(99)


# In[13]:


# append the item at the end of the list.
bacon


# ## 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[15]:


bacon=[3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')  # remove first occurrence of item
bacon


# ## 9. What are the list concatenation and list replication operators?

# Ans: The operator for list concatenation is +, while the operator for replication is *.

# In[16]:


# list concatination

list1=[1,2]
list2=["varsha",3]

list1+list2


# In[19]:


# list replication
l=[4,2]

l*2


# ## 10. What is difference between the list methods append() and insert()?

# Ans: While append() will add values only to the end of a list, insert() can add them anywhere in the list

# In[21]:


# append add at the last

l=['varsha',3,4,5,True]
l.append(False)
l


# In[23]:


# insert add item with its index value

l=['varsha',3,4,5,True]
l.insert(2,False)
l


# ## 11. What are the two methods for removing items from a list?

# remove(item) - removeds first occurence of a item
# pop() - Remove and returns item at index (default last).
# 

# In[24]:


l=[2,3,2,5,6,5,6]
l.remove(5)
l


# In[26]:


l=[2,3,2,5,6,5,6]
l.pop()
l


# In[ ]:





# ## 12. Describe how list values and string values are identical.

# 1. Both lists and strings can be passed to len()
# 2. Both have indexes and slices
# 3. Both can be used in for loops
# 4. Both can be concatenated or replicated
# 5. Both can be used with the in and not in operators

# ## 13. What's the difference between tuples and lists?

# Lists :
#         1. are mutable - they can have values added, removed, or changed. 
#         
#         2. list use the square brackets, [  ]
#         
# Tuples :
#         1.are immutable; they cannot be changed . 
#         
#         2.Tuples are written using parentheses, ( ).  

# ## 14. How do you type a tuple value that only contains the integer 42?

# In[28]:


t = (42,)
print(t)


# ## 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# Ans: By using tuple() and list() functions

# In[30]:


# getting tuple from list

l1=[2,3,4,5]
l2=tuple(l1)
print(l2)


# In[35]:


# getting list from tuple

t1=[2,3,4,5]
t2=list(t1)
print(t2)


# In[ ]:





# ## 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

# Ans: They contain references to list values.

# ## 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# Ans: The copy.copy() function will do a shallow copy of a list, while 
#     the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate 
#     any lists inside the list.

# In[ ]:





# In[ ]:




