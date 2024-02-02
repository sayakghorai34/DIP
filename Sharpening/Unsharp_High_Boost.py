import cv2 as cv
import numpy as np

img = cv.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png", 0)
blurred = cv.GaussianBlur(img, (5, 5), 1)
difference = img - blurred
sharpening_factor1 = 0.5 #unsharp masking
sharpening_factor2 = 2   #high-boost filtering
# Apply unsharp masking (or high-boost filtering)
sharpened1 = img + sharpening_factor1 * difference
# keep in range [0, 255]
sharpened1 = np.clip(sharpened1, 0, 255).astype(np.uint8)

sharpened2 = img + sharpening_factor2 * difference
# keep in range [0, 255]
sharpened2 = np.clip(sharpened2, 0, 255).astype(np.uint8)

difference = difference.astype(np.uint8)
cv.imwrite("Input_img.png", img)
cv.imwrite("Unsharp_Out.png", sharpened1)
cv.imwrite("High_Boost_Out.png", sharpened2)
cv.imwrite("Blurred.png", blurred)
cv.imwrite("Difference_Filter.png", difference)
cv.waitKey(0)
cv.destroyAllWindows()
