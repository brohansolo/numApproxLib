import numpy as np


a= np.array([1,2,3,4])
print(a)

b = np.array([[10,12,13,14], [30,40,50,31]])
print(b)

print(a.ndim)
print(b.ndim)
print(b.shape)

print(a.itemsize)
print(b.itemsize)

c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
print(c.size)

#getting a specific element from the array: python indexing starts at 0
# so we use the following notation: <arrayname>[row,col]

print(c[1, 2])

#to get a specific row we have the following <arrayname>[row, :], and for colum we do <arrayname>[:, col]

#we can also set which elements we want selected from the array
# <arrayname>[startindex:endindex:stepsize]

print(c[0, 1:5:2]) #eleemnts are exclusive of end point so this only prints [2,4] instead of [2,4,6]

#creating an array of all 0s
np.zeros([2,3]) #dimension of the array given as argument
#we can also do np.ones
print(np.full((2,2), 41)) #creates an appropriately sized array with 99 as the values

#we can also do np.full_like(a.6)


