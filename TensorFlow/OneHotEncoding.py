#!/usr/bin/env python
# coding: utf-8

# In[54]:


import tensorflow as tf


# In[61]:


x = tf.constant([0,1,2,3,4] , name = "x")


# Using One Hot Encodings

# In[56]:


def one_hot_encoding(a, dep, axi):
    ohe = tf.one_hot(a, depth = dep, axis = axi, name = "ohe")
    sess = tf.Session()                   # Create a session
    print("One hot encoding of a with ",dep," depth/classes and axis = ",axi," : ")
    print(sess.run(ohe)  )               # Prints the one_hot encoding output
    sess.close()


# In[62]:


one_hot_encoding(a=x , dep=5 , axi=-1)


# In[63]:


one_hot_encoding(a=x , dep=5 , axi=1)


# In[64]:


one_hot_encoding(a=x , dep=5 , axi=0)


# In[65]:


one_hot_encoding(a=x , dep=6 , axi=0)


# In[66]:


one_hot_encoding(a=x , dep=6 , axi=1)


# In[67]:


one_hot_encoding(a=x , dep=6 , axi=-1)


# In[68]:


one_hot_encoding(a=x , dep=3 , axi=0)


# In[70]:


one_hot_encoding(a=x , dep=3 , axi=1)


# In[ ]:




