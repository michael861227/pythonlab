import numpy as np
import matplotlib.pyplot as plt
#0~3切20個點
x = np.linspace(0, 3, 20)
#0~9切20個點
y = np.linspace(0, 9, 20)

#印線
plt.plot(x, y)

#印點
plt.plot(x,y,"ro")
plt.show()