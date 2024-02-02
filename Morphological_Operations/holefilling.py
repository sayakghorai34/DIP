import cv2
import numpy as np

# Read the input image in grayscale
input_image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Morphological_Operations/image.jpeg', cv2.IMREAD_GRAYSCALE)

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

# Create the negation of the hole mask
hole_mask = input_image - erosion(input_image, structuring_element)

# Initialize X0 with a single white pixel belonging to the hole
X0 = np.zeros_like(input_image, dtype=np.uint8)
X0[0, 0] = 255

# Iterate to dilate Xn and update it with the intersection of Xn and negation of the hole mask
Xn = X0.copy()

while not np.array_equal(Xn, dilation(Xn, structuring_element)):
    Xn = np.minimum(dilation(Xn, structuring_element), cv2.bitwise_not(hole_mask))

# Final result is the union of the original hole mask and Xn
final_result = cv2.bitwise_or(hole_mask, Xn)

# Display the resulting images
cv2.imshow('Original Image', input_image)
cv2.imshow('Hole Mask', hole_mask)
cv2.imshow('Final Result', final_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
