import cv2
import numpy as np
input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Invert.png")
output_img = 255 - input_img
gap = input_img - input_img
Out = np.concatenate((input_img,gap,output_img),1)
cv2.imshow('Input-Output',Out)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('NegetiveOut.jpeg',output_img)
    cv2.destroyAllWindows()
