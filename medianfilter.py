#!/usr/bin/env python
# coding: utf-8

# In[53]:



get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import SimpleITK as sitk


fig = plt.figure(figsize=(12,8))  #is to create a figure object.
a = fig.add_subplot(1, 2, 1)
a.set_title('Input')
img1 = sitk.ReadImage("C:/Users/User/Desktop/nat.jpg") #path to a File
npa1 = sitk.GetArrayViewFromImage(img1) #returns an immutable numpy array view to the data.

plt.imshow(npa1,cmap=plt.cm.Greys_r);


img = sitk.ReadImage("C:/Users/User/Desktop/nat.jpg")
median_filter = sitk.MedianImageFilter()
median_filter.SetRadius(5)
smoothed = median_filter.Execute(img)
a = fig.add_subplot(1, 2, 2)
a.set_title('Output')
npa_zslice = sitk.GetArrayViewFromImage(smoothed)
plt.imshow(npa_zslice,cmap=plt.cm.Greys_r)



# In[ ]:




