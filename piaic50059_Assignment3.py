#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def function1():
    x=np.arange(1,13).reshape((6,2))
    return x


# In[3]:


function1()


# In[4]:


def function2():
    y=np.arange(10,37,dtype=np.float64).reshape((3,3,3))
    return y


# In[5]:


function2()


# In[6]:


def function3():
    a = np.arange(1, 100*10+1).reshape((100,10))
    x=a[[3,6,10,13,17,20,24,27,31,34,38,41,45,48,52,55,59,62,66,69,73,76,80,83,87,90,94,97],[4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9,4,9]]
    return x


# In[7]:


function3()


# In[8]:


def function4():
    arr_1 = np.arange(9).reshape(3,3)
    arr_1[:,[0,1]]=arr_1[:,[1,0]]
    return arr_1


# In[9]:


function4()


# In[10]:


def function5():
    z=np.zeros((4,5))
    return z


# In[11]:


function5()


# In[12]:


def function6():
    arr=np.arange(10)
    arr[[6,8]]=10,20
    return arr


# In[13]:


function6()


# In[14]:


def function7():
    y=np.arange(4,dtype=np.int64)
    z=np.zeros_like(y)
    return z


# In[15]:


function7()


# In[16]:


def function8():
    x=np.arange(12,dtype=np.uint32).reshape(2,6)
    x[:]=[6]
    return x


# In[17]:


function8()


# In[18]:


def function9():
    return np.arange(2,102,2)


# In[19]:


function9()


# In[20]:


def function10():
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subtruct=arr-np.vstack(brr)
    return subtruct


# In[21]:


function10()


# In[22]:


def function11():
    arr=np.arange(10)
    arr[[1,3,5,7,9]]=-1
    return arr


# In[23]:


function11()


# In[24]:


def function12():
    arr=np.array([1,2,3])
    repeat=np.repeat(arr,3)
    tile=np.tile(arr,3)
    ans=np.concatenate((repeat,tile))
    return ans


# In[25]:


function12()


# In[26]:


def function13():
    arr=np.array([2,6,1,9,10,3,27])
    ans=arr[[1,3]]
    return ans


# In[27]:


function13()


# In[28]:


def function14():
    arr1=np.arange(10,34,1).reshape(8,3)
    ans=np.split(arr1,4)
    return ans


# In[29]:


function14()


# In[36]:


def function15():
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    arr2=np.sort(arr,axis=0)
    arr2[[0,1,1,2],[2,0,2,0]]=arr[[1,0,0,2],[2,0,2,0]]
    return arr2


# In[37]:


function15()


# In[38]:


def function16():
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    z=np.concatenate((x,y),axis=1)
    ans=print(z)
    return ans


# In[39]:


function16()


# In[41]:


def function17():
    arr = np.arange(1,10*10+1).reshape((10,10))
    ans=np.where((arr%5==0)&(arr%3==0),'Yes','No')
    return ans


# In[42]:


function17()


# In[43]:


def function18():
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    msk=np.isin(piaic,students)
    ans=piaic[msk]
    return ans


# In[44]:


function18()


# In[45]:


def function19():
    x=np.arange(1,26).reshape(5,5)
    w=np.copy(x)
    w=w.T
    b=5
    ans=(x*w)+b
    return ans


# In[46]:


function19()


# In[47]:


def function20():
    x=np.arange(1,11)
    def abc():
        print(x*2+3-2)
    abc()


# In[48]:


function20()


# In[ ]:




