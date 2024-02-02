import cv2
import numpy as np

image = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png",cv2.IMREAD_UNCHANGED)
image2 = np.zeros_like(image)
image3 = np.zeros_like(image)
cv2.imshow('Input',image)
# hsi_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# # G = float(input("Enter Gamma\n(>1Emphasize Higher Intensity\n<1Emphasize Lower Intensity )\n»"))
# G = 0.5
# hsi_img[:,:,2] = 15*np.power(hsi_img[:,:,2],G)
# res = cv2.cvtColor(hsi_img,cv2.COLOR_HSV2BGR)

G1 = 0.5
image2[:,:,0] = 2*np.power(image[:,:,0],G1)        
image2[:,:,1] = 2*np.power(image[:,:,1],G1)
image2[:,:,2] = 2*np.power(image[:,:,2],G1)
contrast_r = np.max(image2[:,:,0]) - np.min(image2[:,:,0])
contrast_g = np.max(image2[:,:,1]) - np.min(image2[:,:,1])
contrast_b = np.max(image2[:,:,2]) - np.min(image2[:,:,2])
for i in range(image2.shape[0]):
    for j in range(image2.shape[1]):
        image2[i,j][0] = 255*(image2[i,j][0]-np.min(image2[:,:,0]))/(contrast_r)
        image2[i,j][1] = 255*(image2[i,j][1]-np.min(image2[:,:,1]))/(contrast_g)
        image2[i,j][2] = 255*(image2[i,j][2]-np.min(image2[:,:,2]))/(contrast_b)

G2 = 1.5
image3[:,:,0] = 2*np.power(image[:,:,0],G2)
image3[:,:,1] = 2*np.power(image[:,:,1],G2)
image3[:,:,2] = 2*np.power(image[:,:,2],G2)
contrast_r = np.max(image2[:,:,0]) - np.min(image2[:,:,0])
contrast_g = np.max(image2[:,:,1]) - np.min(image2[:,:,1])
contrast_b = np.max(image2[:,:,2]) - np.min(image2[:,:,2])
for i in range(image2.shape[0]):
    for j in range(image2.shape[1]):
        image3[i,j][0] = 255*(image3[i,j][0]-np.min(image3[:,:,0]))/(contrast_r)
        image3[i,j][1] = 255*(image3[i,j][1]-np.min(image3[:,:,1]))/(contrast_g)
        image3[i,j][2] = 255*(image3[i,j][2]-np.min(image3[:,:,2]))/(contrast_b)


cv2.imshow('Gamma 0.5',image2)
cv2.imshow('Gamma 1.5',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()


