
import SimpleITK as sitk
import sys
from  image_viewing import *


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('No input and/or output image filename given!')
        print('Usage: python ' + str(sys.argv[0]) + ' <input filename> <output filename> ')
        exit(-1)






# load example image from argv
reader = sitk.ImageFileReader()
reader.SetFileName(sys.argv[1])
input_image  = reader.Execute()
show_image(input_image, 'Input Image', blocking=False)


#smoothing-processing
clurFilter = sitk.CurvatureFlowImageFilter()
clurFilter.SetNumberOfIterations(5)
clurFilter.SetTimeStep(0.125)
smoothed = clurFilter.Execute(input_image)
show_image(smoothed, 'Smoothed', blocking=False)

# seedpoints
seeds = show_and_return_markers(smoothed, 'Set Seedpoints')
print('seedpoints:', seeds)


# segmentation

segmentation = sitk.ConfidenceConnectedImageFilter()
segmentation.SetSeedList(seeds)
segmentation.SetMultiplier(1)
segmentation.SetInitialNeighborhoodRadius(4)
seg = segmentation.Execute(smoothed)

show_image(seg, 'segmentation', blocking=False)



# fill holes and remove small connected components
vector = (1, 1, 1)
kernel = sitk.sitkBall
morphologicalClosing = sitk.BinaryMorphologicalClosing(seg, vector, kernel)
show_image(morphologicalClosing, 'MorphologicalClosing', blocking=False)


image_Cast = sitk.Cast(morphologicalClosing, sitk.sitkInt16)
overlap = sitk.LabelOverlapMeasuresImageFilter()
overlap.Execute(input_image,image_Cast)
print("\nVolume: " , overlap.GetVolumeSimilarity())
print("Dice: " , overlap.GetDiceCoefficient())





# visualize result
show_image_with_mask(input_image, morphologicalClosing, 'Result', color='b')
writer = sitk.ImageFileWriter()
writer.SetFileName(sys.argv[2])
writer.Execute(morphologicalClosing)
