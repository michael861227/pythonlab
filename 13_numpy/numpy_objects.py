import numpy as np 
import matplotlib.pyplot as plt

arr = np.arange(10)
print(arr)
print(arr.ndim)
print(arr.shape)

arr2_x = np.arange(5,100,2)
arr2_y = arr2_x**2+1
print(arr2_x)
print(arr2_y)

#plt.plot(arr2,arr2_1,linestyle='--',marker='o',color='b')
#plt.plot(arr2_x,arr2_y,'--bo')
#markers: https://matplotlib.org/api/markers_api.html


arr3_x = np.arange(5,100,3)
arr3_y = 100*arr3_x + 5

plt.plot(arr2_x,arr2_y,'-r',arr3_x,arr3_y,'--bo')
plt.show()


arr4_x = np.linspace(0,10,21)
arr4_y1 = arr4_x *2
arr4_y2 = arr4_x *3

plt.plot(arr4_x,arr4_y1,'-rv',arr4_x,arr4_y2,'-bo')
plt.show()