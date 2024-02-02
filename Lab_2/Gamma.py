import cv2
import numpy as np
input_img = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Gamma.jpg',cv2.IMREAD_GRAYSCALE)
print(input_img)
G = float(input("Enter Gamma\n(>1Emphasize Higher Intensity\n<1Emphasize Lower Intensity )\n»"))
output_img = 15*np.power(input_img,G)
gap = input_img - input_img
im = np.concatenate((input_img,gap,output_img),1)

cv2.imshow('Input-Output', im.astype(np.uint8))  # Convert image to suitable data type
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('GammaOut.jpeg', im)
    cv2.destroyAllWindows()