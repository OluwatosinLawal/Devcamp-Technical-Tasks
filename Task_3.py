#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Prime numbers are numbers that are only divisible by 1 and itself
#the solution from task_2 will be used to iterate through the arrays

def is_it_prime (array):
    array_list = []
    prime_numbers = True
    for item in array:
        if item > 1:        #Again, we put the formula for the prime number into the code
            if item/item == 1:
                if item/1 == item:
                    if item%2 != 0:
                        array_list.append(item)
    return array_list
is_it_prime([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])     #As we know, 1 is not a prime number

