###
# Draws the function y = sin(x) for an angle in the range 0-360 degrees
#
import math
import matplotlib.pyplot as plt

x = []
y = []

for angle in range(0, 361):
    x = x + [angle]
    y = y + [math.sin(math.radians(angle))]

plt.plot(x, y)
plt.show()
