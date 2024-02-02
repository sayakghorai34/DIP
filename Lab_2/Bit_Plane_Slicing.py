import cv2
import numpy as np
gray_img = cv2.imread('/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/BitPlane.jpg', cv2.IMREAD_GRAYSCALE)
height, width = gray_img.shape
bit_planes = np.zeros((8, height, width), dtype=np.uint8)
for i in range(8):
    bit_planes[i] = (gray_img >> i) & 1
bit_planes_display = bit_planes.reshape(2, 4, height, width)
bit_planes_display = np.concatenate(bit_planes_display, axis=1)
bit_planes_display = np.concatenate(bit_planes_display, axis=1)
cv2.imshow('Bit Planes (2x4)', bit_planes_display * 255)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Bit_Plane_Sliced_Output.jpg',bit_planes_display*255)
    cv2.destroyAllWindows()