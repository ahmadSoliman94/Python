#!/usr/bin/env python
# coding: utf-8

# In[1]:


import SimpleITK as sitk
import sys

# only run code if executed as python script
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('No input and/or output image filename given!')
        print('Usage: python ' + str(sys.argv[0]) + ' <input filename> <output filename>')
        exit(-1)

    # get input and output filename
    input_image_filename = sys.argv[1]
    output_image_filename = sys.argv[2]

    # define reader and load image
    reader = sitk.ImageFileReader()
    reader.SetFileName(input_image_filename)
    input_image = reader.Execute()

    ##########################################
    # TODO: Task 1
    # Add sitk.GradientMagnitudeImageFilter to the pipeline
    gardient = sitk.GradientMagnitudeImageFilter()
    smoothed = gardient.Execute(input_image)
    
    
    #   or apply the sitk.GradientMagnitude method to the image
    ##########################################

    # define writer and save image
    writer = sitk.ImageFileWriter()
    writer.SetFileName(output_image_filename)
    writer.Execute(smoothed)


# In[21]:


import SimpleITK as sitk
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt



img = sitk.ReadImage("C:/Users/User/Desktop/SITKTutorialExercises/images/lungCT.mhd")
grad = sitk.GradientMagnitudeImageFilter()
g = grad.Execute(img)


# Display the image slice from the middle of the stack, z axis
#z = int(mr_image.GetDepth()/2)
npa_zslice = sitk.GetArrayViewFromImage(g)

# Three plots displaying the same data, how do we deal with the high dynamic range?
#fig = plt.figure(figsize=(10,3))

#fig.add_subplot(1,3,1)
#plt.imshow(npa_zslice)
#plt.title('default colormap', fontsize=10)
#plt.axis('off')

fig.add_subplot(1,3,2)
plt.imshow(npa_zslice,cmap=plt.cm.Greys_r);
#plt.title('grey colormap', fontsize=10)
#plt.axis('of')

#fig.add_subplot(1,3,3)
#plt.title('grey colormap,\n scaling based on volumetric min and max values', fontsize=10)
#plt.imshow(npa_zslice,cmap=plt.cm.Greys_r, vmin=npa.min(), vmax=npa.max())
#plt.axis('off');


# In[ ]:




