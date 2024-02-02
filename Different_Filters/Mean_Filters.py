import cv2
import numpy as np

image = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_5/Lenna.png", 0)


def arithmatic_mean(img, size):
    out = np.zeros_like(img, dtype=np.float64)
    padding = int(size / 2)
    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[1] - padding):
            window = img[
                i - padding : i + padding + 1,
                j - padding : j + padding + 1,
            ]
            sum = 0.0
            for x in range(size):
                for y in range(size):
                    sum += window[x, y]

            out[i, j] = sum * (1.0 / (size * size))
    return out

def contraharmonic_mean(img, size, Q):
    out = np.zeros_like(img, dtype=np.float64)
    padding = int(size / 2)
    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[1] - padding):
            window = img[i - padding : i + padding + 1, j - padding : j + padding + 1]
            num_sum = 0.0
            den_sum = 0.0
            for x in range(size):
                for y in range(size):
                    value = window[x, y]
                    num_sum += value ** (Q + 1)
                    den_sum += value**Q
            out[i, j] = num_sum / (den_sum + 1e-10)
    return out
def geometric_mean(img, size):
    out = np.zeros_like(img, dtype=np.float64)
    padding = int(size / 2)
    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[1] - padding):
            window = img[
                i - padding : i + padding + 1,
                j - padding : j + padding + 1,
            ]
            product = 1.0
            for x in range(size):
                for y in range(size):
                    product *= window[x, y]
            out[i, j] = product ** (1.0 / (size * size))
    return out

def harmonic(img, size):
    out = np.zeros_like(img, dtype=np.float64)
    padding = int(size / 2)
    for i in range(padding, img.shape[0] - padding):
        for j in range(padding, img.shape[1] - padding):
            window = img[
                i - padding : i + padding + 1,
                j - padding : j + padding + 1,
            ]
            rec_sum = 0.0
            for x in range(size):
                for y in range(size):
                    rec_sum += 1 / window[x, y]
            out[i, j] = int((size * size) / rec_sum)
    return out

size = 7
Q = 1

out1 = contraharmonic_mean(img=image, size=size, Q=Q).astype(np.uint8)
out2 = arithmatic_mean(image, size=size).astype(np.uint8)
out3 = geometric_mean(image, size=size).astype(np.uint8)
out4 = harmonic(image, size=size).astype(np.uint8)

cv2.imwrite("Input_img.png", image)
cv2.imwrite("Contraharmonic_Mean_Out.png", out1)
cv2.imwrite("Arithmatic_Mean_Out.png", out2)
cv2.imwrite("Geometric_Mean_Out.png", out3)
cv2.imwrite("Harmonic_Mean_Out.png", out4)
