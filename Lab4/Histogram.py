import numpy as np
import matplotlib.pyplot as plt
import cv2
# arr = np.random.randint(0,255,64).reshape(8,8)
arr = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab4/lena_dark.png",cv2.IMREAD_GRAYSCALE)    #/Users/sayakghorai/Desktop/DIP_Codes/Lab4/lena_dark.png
# print(arr)


x_axis = [i for i in range(0,256)]  #intensity levels
y_axis = []  #Pixels at the intensity levels
for k in x_axis:
    count = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i,j] == k:
                count+=1
    y_axis.append(count)
# print(y_axis)

hist = cv2.calcHist([arr],[0],None,[256],[0,256])


figure, axis = plt.subplots(1, 2)
  
# For my function
axis[0].plot(x_axis, y_axis,color = 'red')
axis[0].set_title("Without Function")
  
# For library function
axis[1].plot(hist,color = 'blue')
axis[1].set_title("With Function")

  
# Combine all the operations and display
plt.show()


