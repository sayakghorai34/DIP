import numpy as np
import cv2

def approx(num):
    if(num-int(num)>=0.5):
        return int(num)+1
    return int(num)

# arr = np.arange(0,256,1).reshape(16,16)
# res = np.zeros_like(arr)
arr = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_3/Invert.png",cv2.IMREAD_GRAYSCALE)
res = arr - arr
gap = arr - arr
# print("Input Matrix»»\n")
# print(arr)
# print(arr[2,1])

intensity_r = [i for i in range(101,151)]
intensity_s = [(200 - 3*i) for i in range(1,51)]

intensity_r2 = [i for i in range(150,256)]
intensity_s2 = [(50-i*(50/105)) for i in range(0,106)]

# print(intensity_r.index(102))
# print(arr.shape)
# print(intensity_s[intensity_r.index(arr[i,j])])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if 0<=arr[i,j]<=100:
            res[i,j] = approx(255 - arr[i,j]*0.55)
        elif 100<arr[i,j]<=150:
            res[i,j] = approx(intensity_s[intensity_r.index(arr[i,j])])
        elif 150<=arr[i,j]<=255:
            res[i,j] = approx(intensity_s2[intensity_r2.index(arr[i,j])])

# print("output")
# print(res)

Out = np.concatenate((arr,gap,res),1)
cv2.imshow('Input-Output',Out.astype(np.uint8))
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Intensity_Lebel_Output.jpg',res)
    cv2.destroyAllWindows()