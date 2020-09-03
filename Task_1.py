#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_arrays (arrays): #This defines the function of summing an array
    even_sum = 0            #This gives the initial value for the even sum
    odd_sum = 0             #This gives the initial value for the odd sum
    for numbers in arrays:  #This iterates the array i.e continuosly selects number from the beginning till the end
        if numbers%2 == 0:   #The if statement helps condition the number if it is an even number
            even_sum = even_sum + numbers
        else:           #This helps to condition the number if it returns false
                odd_sum = odd_sum + numbers
    return even_sum, odd_sum
            
sum_of_arrays([1,2,3,4,5,6,7,8,9,10])


# In[ ]:





# In[ ]:




