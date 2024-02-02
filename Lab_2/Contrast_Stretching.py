import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Contrast.jpeg",cv2.IMREAD_GRAYSCALE)
# print(input_img)
output_img = np.zeros((input_img.shape[0],input_img.shape[1]),dtype = 'uint8')
# print(output_img)
img_min,img_max = np.min(input_img),np.max(input_img)
contrast = img_max-img_min
for i in range(input_img.shape[0]):
    for j in range(input_img.shape[1]):
        output_img[i,j] = 255*(input_img[i,j]-img_min)/(contrast-5)
gap = input_img - input_img
Out = np.concatenate((input_img,gap,output_img),1)
cv2.imshow('Input-Output',Out.astype(np.uint8))
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Contrast_Stretched_Output.jpg',output_img)
    cv2.destroyAllWindows()