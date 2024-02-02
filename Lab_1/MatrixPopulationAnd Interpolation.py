import numpy as np
import random
src_dim = 4                     #Source image/matrix dimention
tar_dim = 8                 #Target image/matrix dimention

src_matrix = [[None for _ in range(src_dim)] for _ in range(src_dim)] #Creating Empty Source Matrix of src_dim * src_dim dimention
for i in range(src_dim):
    for j in range(src_dim):
        src_matrix[i][j] = random.randrange(0,255,1)       #populating the Array/Matrix

tar_matrix = [[None for _ in range(tar_dim)] for _ in range(tar_dim)] #Creating Empty Target Matrix of target_dim * target_dim dimention
# print(tar_matrix)
#Maping Corners from src »» tar matrix
tar_matrix[0][0] = src_matrix[0][0]
tar_matrix[0][tar_dim - 1] = src_matrix[0][src_dim - 1]
tar_matrix[tar_dim - 1][0] = src_matrix[src_dim - 1][0]
tar_matrix[tar_dim - 1][tar_dim - 1] = src_matrix[src_dim - 1][src_dim - 1]
# print(src_matrix,"\n\n\n\n",tar_matrix)

# forward maping other elements from src »» tar matrix 
multiplier = int(tar_dim/src_dim)

for i in range(1,src_dim-1):
    tar_matrix[0][multiplier * i] = src_matrix[0][i]
for i in range(1,src_dim-1):
    for j in range(0,src_dim):
        tar_matrix[multiplier * i][multiplier * j] = src_matrix[i][j] 
for i in range(1,src_dim-1):
    tar_matrix[tar_dim - 1][multiplier * i] = src_matrix[src_dim - 1][i] 
print(src_matrix,"\n\n\n\n",tar_matrix)



#N4 Neighbourhood Interpolation
def Nx_Interpolation(matrix,choice):
    i_Arr,j_Arr = [],[]
    #offsets for N4
    iA1 = [-1, 0, 1, 0]
    jA1 = [0, -1, 0, 1]
    #offsets for ND
    iA2 = [-1, -1, 1, 1]
    jA2 = [-1, 1, -1, 1]
    #offsets for N8
    iA3 = [-1,-1,-1,0,0,1,1,1]
    jA3 = [-1,0,1,-1,1,-1,0,1]
    
    if(choice == 1):            #N4 Principle
        i_Arr,j_Arr = iA1,jA1
    elif(choice == 2):          #ND Principle
        i_Arr,j_Arr = iA2,jA2
    elif(choice == 3):          #N8 Principle
        i_Arr,j_Arr = iA3,jA3
    
    for i in range(len(matrix)):  # Iterate over rows
        for j in range(len(matrix[0])):  # Iterate over columns
            if matrix[i][j] is None:
                for i_off, j_off in zip(i_Arr, j_Arr):
                    new_i, new_j = i + i_off, j + j_off
                    if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                        if matrix[new_i][new_j] is not None:
                            matrix[i][j] = matrix[new_i][new_j]
                            break
choice = 3
Nx_Interpolation(tar_matrix,choice)
print(f'\n\n\n After N(x={choice})_Interpolation:\n',tar_matrix)

#Remaining Bilinear Interpolation
def bi_interpolation(arr1, x, y):
    arr = np.array(arr1)
    height, width = arr.shape
    x1 = int(x)
    y1 = int(y)
    x2 = x1 + 1
    y2 = y1 + 1
    if x2 >= width:
        x2 = x1
    if y2 >= height:
        y2 = y1
 
    p11 = arr[y1, x1]
    p12 = arr[y2, x1]
    p21 = arr[y1, x2]
    p22 = arr[y2, x2]
 
    x_diff = x - x1
    y_diff = y - y1
 
    interpolated = (p11 * (1 - x_diff) * (1 - y_diff) +
                          p21 * x_diff * (1 - y_diff) +
                          p12 * (1 - x_diff) * y_diff +
                          p22 * x_diff * y_diff)
 
    return interpolated
for i in range(tar_dim):
    for j in range(tar_dim):
        if tar_matrix[i][j] is None:
            tar_matrix[i][j] = int(bi_interpolation(src_matrix,i/2,j/2))
print('\n\n\n\n',tar_matrix)