import cv2
import numpy as np

# Read the input image in grayscale
input_image = cv2.imread(r'/Users/sayakghorai/Desktop/DIP_Codes/Morphological_Operations/image.jpeg', cv2.IMREAD_GRAYSCALE)

# Define structuring element (kernel) for morphological operations
kernel_size = 5
structuring_element = np.ones((kernel_size, kernel_size), dtype=np.uint8)

# Function for Dilation operation
def dilation(image, structuring_element):
    height, width = image.shape
    output = np.zeros((height, width), dtype=np.uint8)
    k_height, k_width = structuring_element.shape
    k_center_x, k_center_y = k_width // 2, k_height // 2
    for i in range(0, height):
        for j in range(0, width):
            try:
                roi = image[i - k_center_y:i + k_center_y + 1, j - k_center_x:j + k_center_x + 1]
                output[i, j] = np.max(roi)
            except:
                continue
    return output

# Function for Erosion operation
def erosion(image, kernel):
    height, width = image.shape
    output = np.zeros((height, width), dtype=np.uint8)
    k_height, k_width = kernel.shape
    k_center_x, k_center_y = k_width // 2, k_height // 2
    for i in range(0, height):
        for j in range(0, width):
            try:
                roi = image[i - k_center_y:i + k_center_y + 1, j - k_center_x:j + k_center_x + 1]
                output[i, j] = np.min(roi)
            except:
                continue
    return output

# Perform Dilation
dilated_image = dilation(input_image, structuring_element)

#perform Erosion
eroded_image = erosion(input_image, structuring_element)

# Perform Erosion on the dilated image
closed_image = erosion(dilated_image, structuring_element)

# Display the resulting image
cv2.imshow('Original Image', input_image)
cv2.imshow('Morphological Dilation', dilated_image)
cv2.imshow('Morphological Erosion', eroded_image)
cv2.imshow('Morphological Closing', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
