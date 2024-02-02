import cv2 as cv
import numpy as np


# Load the grayscale image
img = cv.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png", 0)

def gaussian_filter(img, kernel_size, sigma):
    # Create a Gaussian kernel
    kernel = np.zeros((kernel_size, kernel_size))
    center = kernel_size // 2
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - center, j - center
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= kernel.sum()
    filtered_img = np.zeros_like(img, dtype=np.float64)
    for i in range(center, img.shape[0] - center):
        for j in range(center, img.shape[1] - center):
            region = img[
                i - center : i + center + 1,
                j - center : j + center + 1,
            ]
            filtered_img[i, j] = np.sum(region * kernel) 
    filtered_img = np.clip(filtered_img, 0, 255).astype(np.uint8)
    return filtered_img

kernel_size = 5
sigma = 1.5

filtered_img = gaussian_filter(img, kernel_size, sigma)

cv.imshow("Input", img)
cv.imshow("Gaussian Filter Output", filtered_img)
cv.waitKey(0)
cv.destroyAllWindows()
