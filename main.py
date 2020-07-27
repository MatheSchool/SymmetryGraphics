import math
import numpy as np
import matplotlib.pyplot as plt

triangulo1 = [[1, 0], [4,0], [3,-5], [1,0]]

x1 = [point[0] for point in triangulo1]
y1 = [point[1] for point in triangulo1]

simetria1 = np.matrix([[-1/2, math.sqrt(3)/2], [math.sqrt(3)/2, 1/2,]]);

print (simetria1)

plt.plot(x1,y1, 'b')
plt.plot(x1,y1, 'bo')

print (triangulo1)
print (np.transpose(triangulo1))

triangulo2 = np.array(np.transpose(simetria1 * np.transpose(triangulo1)));

print (triangulo2)

x2 = [point[0] for point in triangulo2]
y2 = [point[1] for point in triangulo2]

plt.plot(x2,y2, 'r')
plt.plot(x2,y2, 'ro')

#np.linalg.norm()

plt.axis([-6, 6, -6, 6])
plt.show()