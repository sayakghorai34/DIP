import cv2
import numpy as np

img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Morphological_Operations/morph.png", 0)

def erotion(img, kernel):
    output = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            result = np.logical_and(neighborhood, kernel)
            if np.all(result):
                output[i, j] = 255

    return output

def dilation(img, kernel):
    output = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            result = np.logical_and(neighborhood, kernel)
            if np.any(result):
                output[i, j] = 255

    return output


def opening(image, kernel):
    result = erotion(image, kernel)
    result = dilation(result, kernel)
    return result


def closing(image, kernel):
    result = dilation(image, kernel)
    result = erotion(result, kernel)
    return result


structe_element = np.ones((3,3), np.uint8)

erosion_out = erotion(img, structe_element)
dilation_out = dilation(img, structe_element)
opening_out = opening(img, structe_element)
closing_out = closing(img, structe_element)

cv2.imwrite("Dilation_Out.png", dilation_out)
cv2.imwrite("Erosion_Out.png", erosion_out)
cv2.imwrite("Opening_Out.png", opening_out)
cv2.imwrite("Closing_Out.png", closing_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
