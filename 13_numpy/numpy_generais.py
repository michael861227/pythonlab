import numpy as np 
import matplotlib.pyplot as plt
'''
mat1 = np.zeros((3,4,5))
print(mat1)
print(mat1.ndim)
print(mat1.shape)
print()

mat2 = np.ones((3,3)) *2
'''
'''
mat2_2 = mat2*2
mat2_3 = mat2 * mat2_2 #和線性代數的矩陣乘法不同
mat2_4 = np.matmul(mat2,mat2_2) #線代矩陣乘法

print(mat2)
print(mat2_2)
print(mat2_3)
print(mat2_4)
print()
'''
'''
mat3 = np.eye(3,3)
print(mat2)
print(mat3)
print(mat2*mat3)
print(np.matmul(mat2,mat3))
print()
'''
arr_x = np.arange(10)
a = np.random.rand(10)                 # uniform in [0, 1]
b = np.random.randint(0, 10, 10)      # uniform in [0, 10) with 10 elements
print(a)
print(b)
plt.plot(arr_x,a,'-r^',arr_x,b,'--go')
plt.show()
