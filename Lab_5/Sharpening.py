import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png",cv2.IMREAD_GRAYSCALE)
arr = np.array(input_img)
output_img1 = np.zeros((input_img.shape[0],input_img.shape[1]))
output_img2 = np.zeros((input_img.shape[0],input_img.shape[1]))
# print(output_img)
img_min,img_max = np.min(input_img),np.max(input_img)
contrast = img_max-img_min
for i in range(1,input_img.shape[0]):
    for j in range(1,input_img.shape[1]):
        ele1 = int(input_img[i,j]) - int(input_img[i,j-1])
        ele2 = int(input_img[i,j]) - int(input_img[i-1,j])
        output_img1[i,j] = 255*(ele1-img_min)/(contrast-5)
        output_img2[i,j] = 255*(ele2-img_min)/(contrast-5)
