import random

src_dim_i = int(input("Enter Sample Matrix Dimension(MxN) M(INT): "))                     #Source image/matrix dimention
src_dim_j = int(input("Enter Sample Matrix Dimension(MxN) N(INT): "))
src = [[None for _ in range(src_dim_j)] for _ in range(src_dim_i)] #Creating Empty Source Matrix of src_dim * src_dim dimention
src_matrix = src.copy()
for i in range(src_dim_i):
    for j in range(src_dim_j):
        src_matrix[i][j] = random.randrange(0,255,1)       #populating the Array/Matrix

def interpolation(matrix):
    i_Arr = [-1,-1,-1,0,0,1,1,1]
    j_Arr = [-1,0,1,-1,1,-1,0,1]
    for i in range(len(matrix)):  # Iterate over rows
        for j in range(len(matrix[0])):  # Iterate over columns
            if matrix[i][j] is None:
                neighbours = []
                for i_off, j_off in zip(i_Arr, j_Arr):
                    new_i, new_j = i + i_off, j + j_off
                    if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                        if matrix[new_i][new_j] is not None:
                            neighbours.append(matrix[new_i][new_j])
                if len(neighbours)==0:
                    i_Arr2 = [0,0,0,0,-1,-1,-1,-1,1,1,1,1,-2,-2,-2,-2,2,2,2,2]
                    j_Arr2 = [0,-1,1,-2,2,0,-1,1,-2,2,0,-1,1,-2,2,0,-1,1,-2,2]
                    for i2_off,j2_off in zip(i_Arr2,j_Arr2):
                        new_i2,new_j2 = i+i2_off,j+j2_off
                        if 0 <= new_i2 < len(matrix) and 0 <= new_j2 < len(matrix[0]):
                            if matrix[new_i2][new_j2] is not None:
                                neighbours.append(matrix[new_i2][new_j2]/((abs(i2_off))**2+(abs(j2_off))**2)**0.5) 
                
                matrix[i][j] = int(sum(neighbours)/len(neighbours)) if len(neighbours)!=0 else 0
    
def Print_Matrix(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            print(Matrix[i][j],end = '\t')
        print('\n')
def translession(Matrix , Tx , Ty):             #shift x and y axis offset values Tx and Ty
    tar_matrix = [[None for _ in range(len(Matrix[0]))] for _ in range(len(Matrix))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            try:
                tar_matrix[i+Ty][j+Tx] = Matrix[i][j]
            except:
                continue
    print("Source: ")
    Print_Matrix(Matrix)
    print(f"After shifting x by {Tx},y by {Ty}")
    Print_Matrix(tar_matrix)
    interpolation(tar_matrix)
    return tar_matrix

# res = translession(src_matrix,2,1)
# print("After Interpolation Final Res: ")
# Print_Matrix(res)

def Rotation_Matrix(Matrix,Angle):
    input = Matrix
    if(int(Angle/90) == 0):
        return Matrix
    elif(abs(Angle)==Angle):
        for _ in range(int(Angle/90)):
            transposed = []  
            for row in zip(*input):
                transposed.append(list(row))
            rotated = []
            for row in transposed:
                rotated.append(row[::-1])               #To read the rows in reverse order. -1 in the slicer indicates that
            input = rotated
        return rotated
    for _ in range(4-int(abs(Angle)/90)):
        transposed = []  
        for row in zip(*input):
            transposed.append(list(row))
        rotated = []
        for row in transposed:
            rotated.append(row[::-1])               #To read the rows in reverse order. -1 in the slicer indicates that
        input = rotated
    return rotated

# input = src_matrix
# Print_Matrix(input)
# print("Rotated:")
# Print_Matrix(Rotation_Matrix(input,-90))

def Scaling_Matrix(Matrix,Scaling_Factor):
    def bilinear_interpolation(image, x, y):
        height = len(image)
        width = len(image[0])
        x_floor = int(x)
        y_floor = int(y)
        dx = x - x_floor
        dy = y - y_floor
        neighbors = [(0, 0), (0, 1), (1, 0), (1, 1)]
        interpolated_value = 0
        total_weight = 0
        for dx_n, dy_n in neighbors:
            x_n = x_floor + dx_n
            y_n = y_floor + dy_n
            if x_n < 0 or x_n >= width:
                continue
            if y_n < 0 or y_n >= height:
                continue
            dist_x = 1 - abs(dx - dx_n)
            dist_y = 1 - abs(dy - dy_n)
            weight = dist_x * dist_y
            total_weight += weight
            interpolated_value += weight * image[y_n][x_n]
        interpolated_value /= total_weight  
        return interpolated_value
    Target = [[None for _ in range(len(Matrix[0]))] for _ in range(len(Matrix))]
    for i in range(len(Target)):
        for j in range(len(Target[i])):
            src_i,src_j = i/Scaling_Factor,j/Scaling_Factor
            try:
                value = bilinear_interpolation(Matrix,src_j,src_i)
                if(value - int(value))>0.5:
                    value = int(value) + 1
                else:
                    value = int(value)
            except:
                value = 255
            Target[i][j] = value
    return Target
                
# Scaling = 2         
# input = src_matrix
# Print_Matrix(src_matrix)
# print(f"Zoomed by: {Scaling}x")
# Print_Matrix(Scaling_Matrix(input,Scaling))

choice = 1
while choice == 1 or choice == 2 or choice ==3:
    choice = int(input("1»Translession\n2»Rotation\n3»Scaling\nAnyOtherKey»Exit\nInput?»»"))
    if choice == 1:
        print("Source Matrix:")
        Print_Matrix(src_matrix)
        res1 = translession(src_matrix,int(input("Enter X_Offset(INT): ")),int(input("Enter Y_Offset(INT): ")))
        print("After Interpolation Final Res: ")
        Print_Matrix(res1)
        print('\n')
    elif choice == 2:
        print("Source Matrix: ")
        Print_Matrix(src_matrix)
        res2 = Rotation_Matrix(src_matrix,int(input("Rotate by(+for clock & - for anticlockwise)(Multiple of 90˚): ")))
        print("Rotated Matrix: ")
        Print_Matrix(res2)
        print('\n')
    else:
        print("Source Matrix:")
        Print_Matrix(src_matrix)
        f = float(input("Enter Scaling Factor(+only)(float): "))
        res3 = Scaling_Matrix(src_matrix,f)
        print(f"Scaled Matrix with factor {f}: ")
        Print_Matrix(res3)
        print('\n')