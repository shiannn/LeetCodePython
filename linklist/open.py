import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
Axes = fig.add_subplot(111)
A = [1,2,3]
B = [4,5,2.5]
C = [7,8,9]
a = 0.5
Axes.bar(['a','b','c'],height = A,align = "edge",width = -0.2)
Axes.bar(['a','b','c'],B,align = "edge",width = 0.2)
Axes.bar(['a','b','c'],C,align = "edge",width = 0.)
plt.show()
