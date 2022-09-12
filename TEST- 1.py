#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Test :
#1.Take the user input (age),above 60 (print("seniors"),40-60(print("your message"),2o-40("your message")
a=int(input("age"))



# In[1]:


#2.print first 10 natural numbers using while and for loop 
i = 1
while i <= 10:
    print(i, end='  ')
    i+=1


# In[2]:


#3.WAP to print the multiplication table (ask the user input )
n=1
print("Numbers\t\tSquares")
while(n<=10):
    print(n,"\t\t",n**2)
    n=n+1


# In[3]:


#4.Creat a list of your favourite fruits and print one by one 
fruits = ["banana","orange","apple","dates"]
nl=[]
for x in fruits:
    nl.append(fruits)
print(nl)


# In[14]:


#5 WAP to sum all the items in a list (create a list)

l1=[1,2,3,4]
l2=[3,4,6,7]

zipped_lists = zip(l1, l2)
sum=[l1+l2 for (l1,l2)in zipped_lists]
sum


# In[19]:


#WAP to rverse a list
a=[1,2,3,4,5]
a.reverse()
a


# In[8]:


#WAP to return the maximum of 2 numbers using list comrehension 


# In[9]:


#print the following pattern
1
11
1111
11111


# In[20]:


#generate a python list of all even numbers between 4 to 3o
for num in range (4,30,2):
    print(num)


# In[21]:


#convert 2 lists into 1 dictionary
key_list=["Rohan","harsh","pranav"]
value_list=[5,6,7,8]
dict_from_list = dict(zip(key_list, value_list))
dict_from_list


# In[22]:


#create a tuple with 3 items and assign every value to a variable and print each variable 
name = "rohan"
age = 28
location = "india"

x = (name, age, location)
print(x)


# In[27]:


#what is append , insert and extend ? prove it with example
a=[1,2,3,4,5]
a.append(6)
a


# In[28]:


a.insert(8,9)


# In[29]:


a


# In[36]:


x=[1,2,3]
b=[2,3,4]
x.extend(b)
x


# In[37]:


#create a numpy and print its shape and dimensions 


# In[41]:


import numpy as np
l1=[1,2,3,4]
l2=[5,6,7,8]
a=np.array([l1,l2])
a


# In[42]:


a.shape


# In[46]:


#linspace & arange

num=np.arange(1,10,2)


# In[47]:


num


# In[50]:


num=np.linspace


# In[ ]:




