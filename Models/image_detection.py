import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def find_and_highlight_photo(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edged = cv2.Canny(blurred, 30, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assuming the largest rectangle that fits certain criteria is the photo
    largest_area = 0
    best_rect = None
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        aspect_ratio = w / float(h)
        
        # Check for aspect ratio of a photo and a reasonable area
        if 0.75 < aspect_ratio < 1.3 and area > 1000 and area > largest_area:
            largest_area = area
            best_rect = (x, y, w, h)
    
    if best_rect:
        # Draw a rectangle around the photo region
        x, y, w, h = best_rect
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green rectangle with thickness 2
        
    # Convert to RGB for displaying
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image_rgb, best_rect



def image_detection(image_path):
    # Path to your image
    print("Image path:", image_path)
    filename = os.path.basename(image_path)
    annotated_image, photo_rect = find_and_highlight_photo(image_path)

    if photo_rect is not None:
        plt.figure(figsize=(10, 8))  # Adjust the size as per your requirement
        plt.imsave('pre_version2.png', annotated_image)

        img = cv2.imread('pre_version2.png', 0)
        # ensure binary
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        # save the result
        print(filename)
        path = "./outputs/" + filename + ".png"
        cv2.imwrite(path, img)
        path = "./outputs/"+filename + ".png"
        print("Photo found at:", photo_rect)
        return path
    else:
        print("No photo found in the document.")
        
        
