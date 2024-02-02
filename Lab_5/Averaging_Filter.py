import numpy as np
import cv2

# Load the image in grayscale mode
image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png', cv2.IMREAD_GRAYSCALE)

def average_blur(image,choice):
    height, width = image.shape  # Shape will be (height, width) for grayscale images
    output_image = np.zeros_like(image)
    window = [[]]
    if choice == 1:
        window =[[1, 2, 1],
                 [2, 4, 2],
                 [1, 2, 1]]
    elif choice == 2:
        window =[[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Extract the 3x3 window
            Contributing_Pixels = [
                image[i-1][j-1], image[i-1][j], image[i-1][j+1],
                image[i][j-1], image[i][j], image[i][j+1],
                image[i+1][j-1], image[i+1][j], image[i+1][j+1]
            ]
            
            # Calculate the sum of the window
            window_sum = sum(val * weight for val, weight in zip(Contributing_Pixels, np.ravel(window)))
            
            # Calculate the average of the window
            avg_value = window_sum / np.sum(window)
            
            # Ensure the average is in the valid range
            avg_value = np.clip(int(avg_value), 0, 255)
            
            # Set the output pixel value to the average
            output_image[i, j] = avg_value.astype(np.uint8)
    
    return output_image

def median_blur(image):
    height, width = image.shape  # Shape will be (height, width) for grayscale images
    output_image = np.zeros_like(image)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Extract the 3x3 window
            Contributing_Pixels = [
                image[i-1][j-1], image[i-1][j], image[i-1][j+1],
                image[i][j-1], image[i][j], image[i][j+1],
                image[i+1][j-1], image[i+1][j], image[i+1][j+1]
            ]
            median = np.median(Contributing_Pixels)

            # Ensure the average is in the valid range
            # median = np.clip(int(median), 0, 255)
            
            # Set the output pixel value to the average
            output_image[i, j] = median.astype(np.uint8)
    
    return output_image

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
sigma = 10  # Standard deviation of the Gaussian distribution
# Define the probabilities for salt and pepper noise
salt_probability = 0.008  # Probability of adding salt noise
pepper_probability = 0.008  # Probability of adding pepper noise

# Add noise to the image
s_p_noisy_image = add_salt_and_pepper_noise(image, salt_probability, pepper_probability)
gauss_noisy_image = add_gaussian_noise(image, mean, sigma)
# Perform average blurring using a 3x3 window on the s and p noisy image
blurred_image_average1 = average_blur(s_p_noisy_image,2)
blurred_image_average2 = average_blur(s_p_noisy_image,1)
meadian_blurred1 = median_blur(s_p_noisy_image)

# Perform average blurring using a 3x3 window on the gauss noisy image
blurred_image_average3 = average_blur(gauss_noisy_image,2)
blurred_image_average4 = average_blur(gauss_noisy_image,1)
meadian_blurred2 = median_blur(gauss_noisy_image)
# Display original image, noisy image, and improved (blurred) image
# combined_image = np.hstack((image, noisy_image, blurred_image_average1, blurred_image_average2,meadian_blurred))
# cv2.imshow('Original Image | Noisy Image | Linear Blurred Image | Gaussian_Like Blurred Image | Median Blurred', combined_image)
# cv2.waitKey(0)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     cv2.imwrite('Averaging_Filter_Output.png',combined_image)
#     cv2.destroyAllWindows()

Out1 = np.concatenate((image,s_p_noisy_image,blurred_image_average1,blurred_image_average2,meadian_blurred1),1)
Out2 = np.concatenate((gauss_noisy_image,blurred_image_average3,blurred_image_average4,meadian_blurred2,cv2.medianBlur(gauss_noisy_image, 3)),1)
# Out3 = np.concatenate((blurred_image_average4,meadian_blurred2,np.zeros_like(meadian_blurred1)),1)
final = np.concatenate((Out1,Out2),0)
cv2.imshow('Original|s&p Noisy|Simple Avg|Gauss_Like Avg|Median||Gauss Noise|Simple Avg|Gauss_Like|Median|BuiltinMedian', final)
cv2.waitKey(0)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Averaging_Filter_Output.png',final)
    cv2.destroyAllWindows()
# cv2.imshow('Noisy Image', noisy_image)
# cv2.waitKey(0)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# cv2.imshow('Average Image', blurred_image_average1)
# cv2.waitKey(0)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# cv2.imshow('Gaussian_Like Image', blurred_image_average2)
# cv2.waitKey(0)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# cv2.imshow('Median Image', meadian_blurred)
# cv2.waitKey(0)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
