import numpy as np

a1 = [ [0,1,2,3,4],
      [5,6,7,8,9]]
b1 = [ [10,11,12,13,14],
      [15,16,17,18,19]]
c1 = [ [20,21,22,23,24],
      [25,26,27,28,29]]

r = np.array(a1)
g = np.array(b1)
b = np.array(c1)

img = np.zeros((2,5,3))

# substitution of green channel
img[:,:,1] = g

print(img)


