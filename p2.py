import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

print("Array a:",a)
print("Array b:",b)
print("sum of array a and b:",np.add(a,b))
print("difference of array a and b:",np.subtract(a,b))
print("product of array a and b:",np.multiply(a,b))
print("Division of array a and b:",np.divide(a,b))
print("square root of array a:",np.sqrt(a))
print("exponential of array a :",np.exp(a))

print("Minimum value of array a:",np.min(a))
print("Maximum value of array b:",np.max(b))
print("Mean value of array a:",np.mean(a))
print("SD value of array b:",np.std(b))
c=np.array([[1,2],[3,4],[5,6]])
print("array c:")
print(c)
print("Reshaped array c(2 rows,3 columns):")
print(np.reshape(c,(2,3)))

d=np.array([[1,2,3],[4,5,6]])
print("array d:")
print(d)
print("Transposed array d:")
print(np.transpose(d))



