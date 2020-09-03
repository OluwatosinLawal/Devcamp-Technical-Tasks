#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This will replace the spaces in the sentence with %20
x = "Mr John Smith"      #Allocate a letter to the sentence
x = x.strip()            #This is to trim the string
x= x.replace(' ',"%20")  #This will replace the spaces with %20

print (x)

