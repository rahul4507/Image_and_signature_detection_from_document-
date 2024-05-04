import cv2
import matplotlib.pyplot as plt
from skimage import measure, morphology, color
import numpy as np
import os

# Constants for connected component analysis
constant_parameter_1 = 84
constant_parameter_2 = 250
constant_parameter_3 = 100
constant_parameter_4 = 18

def process_document(input_image_path):
    filename = os.path.basename(input_image_path)
    filename = filename.split('_')[0]
    img = cv2.imread(input_image_path, 0)

    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary

    # Connected component analysis
    blobs = img > img.mean()
    blobs_labels = measure.label(blobs, background=1)

    the_biggest_component = 0
    total_area = 0
    counter = 0
    average = 0.0
    for region in measure.regionprops(blobs_labels):
        if region.area > 10:
            total_area += region.area
            counter += 1
        # take regions with large enough areas
        if region.area >= 250:
            if region.area > the_biggest_component:
                the_biggest_component = region.area

    average = total_area / counter

    # Calculate thresholds for filtering small and large components
    a4_small_size_outlier_constant = ((average / constant_parameter_1) * constant_parameter_2) + constant_parameter_3
    a4_big_size_outlier_constant = a4_small_size_outlier_constant * constant_parameter_4

    # Remove small and large components
    pre_version = morphology.remove_small_objects(blobs_labels, a4_small_size_outlier_constant)
    component_sizes = np.bincount(pre_version.ravel())
    too_small = component_sizes > a4_big_size_outlier_constant
    too_small_mask = too_small[pre_version]
    pre_version[too_small_mask] = 0
    
    plt.imsave('pre_version1.png', pre_version, cmap='gray')
    plt.figure(figsize=(10, 6))
    plt.imshow(pre_version, cmap='gray')
    
    # Display pre_version image
    plt.axis('off')  # Turn off axis

    # Read the pre-version image
    img = cv2.imread('pre_version1.png', 0)
    # Ensure binary
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Save the processed result
    print(filename)
    path = "./outputs/" + filename + ".png"
    cv2.imwrite(path, img)
    path1=filename + ".png"
    # Return the path of the processed image
    return path1
