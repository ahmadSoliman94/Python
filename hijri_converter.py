#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U hijri-converter')



# In[10]:


from hijri_converter import convert
import datetime

x = datetime.datetime.now()
print(x)
j =int(input("year"))
m = int(input("month"))
d = int(input("day"))

h = convert.Gregorian(j,m,d).to_hijri()
print(h)


# In[ ]:




