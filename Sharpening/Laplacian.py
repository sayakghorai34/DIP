import cv2
import numpy as np

image = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png", 0)

def laplacian(img, filter):
    laplacian_out = np.zeros_like(img, dtype=np.float64)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            region = img[
                i - 1 : i + filter.shape[0] - 1,
                j - 1 : j + filter.shape[1] - 1,
            ]
            laplacian_out[i, j] = np.sum(region * filter)
    laplacian_out = np.clip(laplacian_out, 0, 255)
    return laplacian_out


laplacian_kernel = np.array(
    [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0],
    ]
)

flipped_kernel = np.flip(laplacian_kernel, axis=(0, 1))

laplacian_kernel_8 = np.array(
    [
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1],
    ]
)
kernel_diag = np.array(
    [
        [1, 0, 1],
        [0, -4, 0],
        [1, 0, 1],
    ]
)

out1 = laplacian(img=image, filter=laplacian_kernel).astype(np.uint8)
out2 = laplacian(img=image, filter=laplacian_kernel_8).astype(np.uint8)
out3 = laplacian(img=image, filter=kernel_diag).astype(np.uint8)


cv2.imwrite("Input_img.png", image)
cv2.imwrite("N4_laplacian.png", out1)
cv2.imwrite("N8_laplacian.png", out2)
cv2.imwrite("ND_laplacian.png", out3)
