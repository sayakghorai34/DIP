import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Intensity_Slicing.jpg",cv2.IMREAD_GRAYSCALE)
# print(input_img)
output_img = np.zeros((input_img.shape[0],input_img.shape[1]),dtype = 'uint8')
# print(output_img)
img_min,img_max = np.min(input_img),np.max(input_img)
contrast = img_max-img_min
for i in range(input_img.shape[0]):
    for j in range(input_img.shape[1]):
        input_intensity = input_img[i,j]
        if(input_intensity<=255 and input_intensity>220):
            output_img[i,j] = 210
        elif(input_intensity<=220 and input_intensity>=119):
            output_img[i,j] = 120
        elif(input_intensity>75 and input_intensity<119):
            output_img[i,j] = 50
        else:
            output_img[i,j] = 5
gap = input_img - input_img
Out = np.concatenate((input_img,gap,output_img),1)
cv2.imshow('Input-Output',Out.astype(np.uint8))
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Intensity_Lebel_Output.jpg',output_img)
    cv2.destroyAllWindows()