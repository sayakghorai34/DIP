# import numpy as np
# import matplotlib.pyplot as plt
# # import numpy as np
# # mat1=[1,2,3]
# # mat2=[2,3,4]
# # mat3=np.add(mat1,mat2)
# # print(mat3)
# # x = [(p,q) for p in range(0,-5,-1) for q in range(0,-5,-1)]
# # print(x)
# def visualize_matrices(matrices, titles):
#     num_matrices = len(matrices)
#     fig, axes = plt.subplots(1, num_matrices, figsize=(5*num_matrices, 5))

#     for i, (matrix, title) in enumerate(zip(matrices, titles)):
#         im = axes[i].imshow(matrix, cmap='viridis', interpolation='nearest')
#         axes[i].set_title(title)
#         axes[i].axis('off')
#         fig.colorbar(im, ax=axes[i])

#     plt.tight_layout()
#     plt.show()

# # Example input matrix with None values
# input_matrix = [[1, 0, 3, 4],
#                 [0, 6, 0, 8],
#                 [9, 10, 11, 0]]
# input_matrix2 = np.array([[1, 2, 3, 4],
#                          [3, 6, 7, 8],
#                          [9, 10, 11, 12]])

# visualize_matrices([input_matrix,input_matrix2], ["Input Matrix","Output Matrix"])
# # visualize_matrix(input_matrix2, "Output Matrix")

# print(abs(-5))
# input = input_matrix

# for i in range(2):
#     transposed = []
#     print('input: ',input)    
#     for row in zip(*input):
#         print(row)
#         transposed.append(list(row))
#     print(transposed)
    
#     rotated = []
#     for row in transposed:
#         rotated.append(row[::-1])
#     print('\nhh',input,'\nRotated:',rotated)  
#     input = rotated
# def bilinear_interpolation(image, x, y):
#     height = len(image)
#     width = len(image[0])
#     x_floor = int(x)
#     y_floor = int(y)
#     dx = x - x_floor
#     dy = y - y_floor
#     neighbors = [(0, 0), (0, 1), (1, 0), (1, 1)]
#     interpolated_value = 0
#     total_weight = 0
#     for dx_n, dy_n in neighbors:
#         x_n = x_floor + dx_n
#         y_n = y_floor + dy_n
#         if x_n < 0 or x_n >= width:
#             continue
#         if y_n < 0 or y_n >= height:
#             continue
#         dist_x = 1 - abs(dx - dx_n)
#         dist_y = 1 - abs(dy - dy_n)
#         weight = dist_x * dist_y
#         total_weight += weight
#         interpolated_value += weight * image[y_n][x_n]
#     interpolated_value /= total_weight  
#     return interpolated_value

# # Example usage
# original_matrix = [
#     [1,4,5,6,7,8,9],
#     [2,4,3,5,6,7,8],
#     [7,6,8,5,1,2,3],
#     [0,9,8,7,6,5,4],
#     [3,5,4,9,0,8,7]
# ]

# x = 1.2  # Fractional x-coordinate
# y = 3.4  # Fractional y-coordinate

# interpolated_value = bilinear_interpolation(original_matrix, x, y)
# print(f"Interpolated value at ({x}, {y}): {interpolated_value}")

# import numpy as np
# # print(np.log(5))
# print(np.power([4,2,4,4],0.5))


# import cv2
import numpy as np
# input_img = cv2.imread("/Users/sayakghorai/Desktop/DIP_Codes/Lab_2/Gamma.jpg",cv2.IMREAD_GRAYSCALE)
# print(input_img)
# output_img = np.zeros((input_img.shape[0],input_img.shape[1]),dtype = 'uint8')
# print(output_img)
# img_min,img_max = np.min(input_img),np.max(input_img)
# contrast = img_max-img_min
# for i in range(input_img.shape[0]):
#     for j in range(input_img.shape[1]):
#         print(input_img[i,j])
#         output_img[i,j] = 255*(input_img[i,j]-img_min)/(contrast-7.5)
# gap = input_img - input_img
# Out = np.concatenate((input_img,gap,output_img),1)
# cv2.imshow('ORIGINAL-Negetive',Out.astype(np.uint8))
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     cv2.imwrite('Thresholded.jpg',output_img)
#     cv2.destroyAllWindows()

# arr = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [2,3,4,5],
#     [7,8,9,0]
# ]
# a = np.array(arr)
# b = []
# print(b)
# for a_ele in a:
#     b_ele = a_ele[::-1]
#     # print(b_ele)
#     b.append(b_ele)
# print(b)
# ar = np.linspace(197,50,49)
# print(ar)
# for i in range(1,50):
    # print(200-3*i)
# arr = np.arange(0,100).reshape(10,10)
# print(arr)
# b = np.zeros_like(arr)
# # print(b)
# for i in range(len(arr)):
#     b_ele = arr[i][::-1]
#     # # print(b_ele)
#     # b.append(b_ele)
#     b[i] = b_ele
# res = b[::-1]
# print('\n\n')
# print(res)
arr =np.array([[1,2,3,2,1],
            [3,5,6,8,6],
            [7,5,4,3,2]]) 
res1 = np.zeros_like(arr)
res2 = np.zeros_like(arr)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        ele1,ele2 = (arr[i,j] - arr[i,j-1]),(arr[i,j] - arr[i-1,j])
        res1[i,j],res2[i,j] = ele1,ele2
        print(ele1,ele2)
print(res1,'\n\n',res2)

def Scale_Up(arr):
    min = np.min(arr)
    return arr+min
print(Scale_Up(res1))
        
    
