import numpy as np
import cv2

# Load the image in grayscale mode
image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Angeogram.jpg', cv2.IMREAD_GRAYSCALE)
def gaussian_blur(image, kernel_size, sigma):
    height, width = image.shape  # Shape will be (height, width) for grayscale images
    output_image = np.zeros_like(image)
    
    # Generate Gaussian kernel
    gaussian_kernel = generate_gaussian_kernel(kernel_size, sigma)
    
    # Iterate over the image
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Extract the window
            window = image[i-1:i+2, j-1:j+2]
            
            # Convolve the window with the Gaussian kernel
            weighted_sum = np.sum(window * gaussian_kernel)
            
            # Set the output pixel value to the weighted sum
            output_image[i, j] = int(weighted_sum)
    
    return output_image

def generate_gaussian_kernel(kernel_size, sigma):
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * np.exp(-((x - (kernel_size-1)/2) ** 2 + (y - (kernel_size-1)/2) ** 2) / (2 * sigma ** 2)),
        (kernel_size, kernel_size)
    )
    kernel /= np.sum(kernel)
    return kernel

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    #add peper noise
    salt_mask = np.random.random(image.shape) < salt_prob
    pepper_mask = np.random.random(image.shape) < pepper_prob

    # Add salt noise
    noisy_image = np.copy(image)
    noisy_image[salt_mask] = 255

    # Add pepper noise
    noisy_image[pepper_mask] = 0
    
    return noisy_image
def add_gaussian_noise(image, mean=0, sigma=25):
    row, col = image.shape
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_image = image + gauss
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Define the mean and standard deviation for Gaussian noise
mean = 0  # Mean of the Gaussian distribution
sigma = 25  # Standard deviation of the Gaussian distribution
kernel_size = 3

# Add Gaussian noise to the image
gauss_noisy_image = add_gaussian_noise(image, mean, sigma)

# Define the probabilities for salt and pepper noise
salt_probability = 0.001  # Probability of adding salt noise
pepper_probability = 0.008  # Probability of adding pepper noise

# Add salt and pepper noise to the image
s_p_noisy_image = add_salt_and_pepper_noise(image, salt_probability, pepper_probability)

# Perform average blurring using a 3x3 window on the noisy image
s_p_blurred_image_average = gaussian_blur(s_p_noisy_image,kernel_size,sigma)
gauss_blurred_image_average = gaussian_blur(gauss_noisy_image,kernel_size,sigma)

# Display original image, noisy image, and improved (blurred) image
combined_image = np.hstack((image, s_p_noisy_image, s_p_blurred_image_average,gauss_noisy_image,gauss_blurred_image_average))
cv2.imshow('Original Image | Noisy Image | Blurred Image', combined_image)
cv2.waitKey(0)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Gaussian_Filter_Output.png',combined_image)
    cv2.destroyAllWindows()