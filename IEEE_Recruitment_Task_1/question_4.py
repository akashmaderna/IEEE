import numpy as np, random#imports numpy and random modules in python

a=np.random.randint(1, 101, (5,5))#generates a 5x5 matrix with random integers from 1 to 100(both inclusive)
print("The randomly generated 5x5 matrix is : \n ")
print(a)
print()
b=a[1:4,1:4]#slices a matrix from 'a' from the 2nd to 4th row and 2nd to 4th column
print(b)
print()

c=b[0,0:3]#slices an array from 'b' of the 1st row
d=b[0:3,2]#slices an array from 'c' of the 3rd column
e=np.dot(c,d)#calculates the dot product of the 1st row and the 3rd column
print("The 1st column is : \n")
print(c)
print()

print("The last row is : \n")
print(d)
print()
print("The dot product of the 1st row and the 3rd column is :\n")
print(e)
