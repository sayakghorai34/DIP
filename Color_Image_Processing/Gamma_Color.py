import cv2
import numpy as np
img = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png',cv2.IMREAD_UNCHANGED)

def gamma(img,G):
    image = np.copy(img)
    max_r = np.max(image[:,:,0])
    max_g = np.max(image[:,:,1])
    max_b = np.max(image[:,:,2])
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            image[i,j][0] = max_r*np.power((image[i,j][0]/max_r),G)
            image[i,j][1] = max_g*np.power((image[i,j][1]/max_g),G)
            image[i,j][2] = max_b*np.power((image[i,j][2]/max_b),G)
    return image
    
cv2.imshow("Gamma = 0.5",gamma(img,0.5))
cv2.imshow("Gamma = 1",gamma(img,1))
cv2.imshow("Gamma = 1.5",gamma(img,1.5))
cv2.imshow("Gamma = 2",gamma(img,2))
cv2.waitKey(0)
cv2.destroyAllWindows()

