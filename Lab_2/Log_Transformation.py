import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/DarkImage.jpeg",cv2.IMREAD_GRAYSCALE)
output_img = 25*np.log(3.5+input_img)
gap = input_img - input_img
im = np.concatenate((input_img,gap,output_img),1)

cv2.imshow('Input-Output', im.astype(np.uint8))  # Convert image to suitable data type
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('LogOut.jpeg', im)
    cv2.destroyAllWindows()