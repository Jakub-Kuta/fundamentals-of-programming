###
# Distance to the horizon: d = 3.57 * sqrt(h)
# h - height of the observer in meters, d - distance in km.
#
import math
h = float(input('Enter your height above the ground in m: '))
d = 3.57 * math.sqrt(h)
print(f'Distance to the horizon: {d:.2f} km')
