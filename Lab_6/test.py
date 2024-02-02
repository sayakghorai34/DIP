import cv2
import numpy as np
image = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_6/imagge.png', cv2.IMREAD_GRAYSCALE)
# def get_struct(i,j):
#     Contributing_Pixels = [
#                 image[i-1][j-1], image[i-1][j], image[i-1][j+1],
#                 image[i][j-1], image[i][j], image[i][j+1],
#                 image[i+1][j-1], image[i+1][j], image[i+1][j+1]
#             ]
#     return Contributing_Pixels
print(image[-1,-1])
# struct = get_struct(0,0)
# print(struct)