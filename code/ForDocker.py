import skimage.measure
from skimage import io, filters 
#import pandas as pd

file = r'input\RPE.tif'
output_file =  r'output\binary.png'

#url = 'https://github.com/sugan89/Introduction_To_Docker/blob/main/BioimageAnalysisExample/RPE.tif?raw=true'
image = io.imread(file)
thresholded_image = skimage.filters.threshold_otsu(image)
binary = image > thresholded_image
io.imsave(output_file, binary)
#perimeter = skimage.measure.perimeter(binary, neighbourhood=4)
#print(f'The perimeter of the binary object is {perimeter}')
