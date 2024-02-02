import cv2
import numpy as np
image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_6/Text.jpeg', cv2.IMREAD_GRAYSCALE).astype(np.uint8)


def get_Binary(image):
    return np.where(image >= 180, 255, 0)

image = get_Binary(image)

def get_struct(i, j):
    cols, rows = np.meshgrid(np.arange(-3, 4), np.arange(-3, 4))
    struct = np.column_stack((rows.ravel() + i, cols.ravel() + j))
    return struct
def erosion(image):
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image[i,j] == 255:
                struct = get_struct(i,j)
                flag = True
                for k in struct:
                    if not (0 <= k[0] < image.shape[0] and 0 <= k[1] < image.shape[1] and image[k[0], k[1]] == 255):
                        flag = False
                        break
                if flag:
                    image[i,j] = 255
                        
    return image
out = erosion(image).astype(np.uint8)
combined_image = np.concatenate((image,out),1).astype(np.uint8)
cv2.imshow('image', combined_image)
cv2.waitKey(0)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Erosion_Output.png',out)
    cv2.destroyAllWindows()
