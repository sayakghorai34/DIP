import cv2
import numpy as np

image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_6/Text.png', cv2.IMREAD_GRAYSCALE).astype(np.uint8)

def get_binary(image):
    return np.where(image >= 210, 255, 0)

def get_struct(i, j):
    rows, cols = np.meshgrid(np.arange(-3, 4), np.arange(-3, 4))
    struct = np.column_stack((rows.ravel() + i, cols.ravel() + j))
    return struct

def erosion(image):
    result = np.zeros_like(image)
    for i in range(0, image.shape[0] - 6):
        for j in range(0, image.shape[1] - 6):
            if image[i + 3, j + 3] == 255:
                struct = get_struct(i + 3, j + 3)
                flag = True
                for k in struct:
                    if not (0 <= k[0] < image.shape[0] and 0 <= k[1] < image.shape[1] and image[k[0], k[1]] == 255):
                        flag = False
                        break
                if flag:
                    result[i + 3, j + 3] = 255

    return result

image = get_binary(image)
out = erosion(image).astype(np.uint8)
combined_image = np.concatenate((image, out), 1).astype(np.uint8)

cv2.imshow('image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
