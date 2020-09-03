#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Prime numbers are numbers that are only divisible by 1 and itself 
def is_it_prime (array):
    prime_numbers = True
    for item in array:
        if item > 1:     #Here we put the formula for the prime number into the code
            for num in range (1,9999):
                if item%num == 1:
                  if item%2 != item%num:
                        return False
            else:
                return True
is_it_prime([5])


# In[6]:


#Prime numbers are numbers that are only divisible by 1 and itself
def is_it_prime (array):
    prime_numbers = True
    for item in array:
        if item > 1:     #Here we put the formula for the prime number into the code
            for num in range (1,9999):
                if item%num == 1:
                  if item%2 != item%num:
                        return False
            else:
                return True
is_it_prime([60])

