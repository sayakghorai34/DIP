import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Angeogram.jpg",cv2.IMREAD_GRAYSCALE)
print(input_img)
threshold_value = int(input("Enter Threshold Value: "))
output_img = np.where(input_img >= threshold_value, 0, 255)
gap = input_img - input_img
Out = np.concatenate((input_img,gap,output_img),1)
cv2.imshow('Input-Output',Out.astype(np.uint8))
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Thresholded.jpg',output_img)
    cv2.destroyAllWindows()
