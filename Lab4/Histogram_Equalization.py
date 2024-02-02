import numpy as np
import matplotlib.pyplot as plt
import cv2

def approx(num):
    if(num-int(num)>=0.5):
        return int(num)+1
    return int(num)

arr = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab4/lena_dark.png",cv2.IMREAD_GRAYSCALE)    #/Users/sayakghorai/Desktop/DIP_Codes/Lab4/lena_dark.png
# print(arr)
x_axis = [i for i in range(0,256)]  #intensity levels
hist = cv2.calcHist([arr],[0],None,[256],[0,256])
y_axis = hist.flatten().astype(int)

Pr = [ele/(arr.shape[0]*arr.shape[1]) for ele in y_axis]
s_out = []
for k in range(1,len(Pr)):
    s_out.append(approx(sum(Pr[:k])*255))
# print(s_out)
dict = {str(k):v for k,v in zip(x_axis,s_out)}
out_image = np.zeros_like(arr)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        intensity = arr[i, j]  # Get the intensity of the current pixel
        new_intensity = dict[str(intensity)] # Use the dictionary to get the new intensity value
        out_image[i, j] = new_intensity  # Assign the new intensity to the corresponding pixel in the output image

hist = cv2.calcHist([out_image],[0],None,[256],[0,256])
y_axis_out = hist.flatten().astype(int)

plt.plot(x_axis, y_axis,color = 'red')
plt.title("Before Histogram Equalization")
plt.savefig("Hist_in.png")
plt.close()
plt.plot(x_axis, y_axis_out,color = 'blue')
plt.title("After Histogram Equalization")
plt.savefig("Hist_out.png")

Hori = np.concatenate((arr, out_image), axis=1)
cv2.imshow('Input , Output', Hori)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Histogram_Normalized.png',out_image)
    cv2.destroyAllWindows()


