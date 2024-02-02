import cv2 as cv
import numpy as np
import random

img = cv.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png", 0)

def gradient(img, filter_x, filter_y):
    x_grad = np.zeros_like(img, dtype=np.float64)
    y_grad = np.zeros_like(img, dtype=np.float64)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            x_grad[i, j] = np.sum(img[i - 1 : i + 2, j - 1 : j + 2] * filter_x)
            y_grad[i, j] = np.sum(img[i - 1 : i + 2, j - 1 : j + 2] * filter_y)

    return x_grad, y_grad

def robert(img, filter_x, filter_y):
    x_grad = np.zeros_like(img, dtype=np.float64)
    gradient_y = np.zeros_like(img, dtype=np.float64)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            x_grad[i, j] = np.sum(img[i - 1 : i + 1, j - 1 : j + 1] * filter_x)
            gradient_y[i, j] = np.sum(img[i - 1 : i + 1, j - 1 : j + 1] * filter_y)

    return x_grad, gradient_y


# Initialize the gradient images

# sobel
sobel_x = np.array(
    [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]
)
sobel_y = np.array(
    [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]
)

gradx, grady = gradient(img=img, filter_x=sobel_x, filter_y=sobel_y)
sobel = np.sqrt(gradx**2 + grady**2).astype(np.uint8)


# robbert
roberts_x = np.array(
    [
        [1, 0],
        [0, -1],
    ]
)
roberts_y = np.array(
    [
        [0, 1],
        [-1, 0],
    ]
)

gradx_roberts, grady_roberts = robert(img=img, filter_x=roberts_x, filter_y=roberts_y)
gradient_roberts = np.sqrt(gradx_roberts**2 + grady_roberts**2).astype(np.uint8)

# prewitt
prewitt_x = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ]
)
prewitt_y = np.array(
    [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ]
)

gradx_prewitt, grady_prewitt = gradient(img=img, filter_x=prewitt_x, filter_y=prewitt_y)
gradient_prewitt = np.sqrt(gradx_prewitt**2 + grady_prewitt**2).astype(np.uint8)


cv.imwrite("Input_Img.png", img)
cv.imwrite("Sobel_Out.png", sobel)
cv.imwrite("Roberts_Out.png", gradient_roberts)
cv.imwrite("Perwitt_Out.png", gradient_prewitt)
cv.waitKey(0)
cv.destroyAllWindows()
