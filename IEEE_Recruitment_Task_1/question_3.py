import numpy as np, random, sys
choice=int(input("Enter 5 for 5x5 matrix, or enter 0 for NxM size matrix : "))#input for 5x5 or self-chioce dimensions matrix
if  choice == 0:
                 n=int(input('enter value of N(no. of columns) : '))#no. of columns input
                 m=int(input('enter value of M(no. of rows) : '))#no. of rows input
elif choice == 5:
                 n=5#values of n,m entered as 5,5 if 5 is entered
                 m=5
else:
    print('Sorry, wrong values entered. Only enter values 5 or 0.')
    sys.exit()#function ended for wrong values entered
a = np.random.randint(1,101,(n,m))#generates a matrix of dimensions NxM with randomly generated values between 1 and 100(both inclusive).
print()
print("The Randomly generated matrix is : ")
print(a)

b=np.max(a)#gives the maxm value element of the matrix
c=np.min(a)#gives the minm value element of the matrix
d=np.mean(a)#gives the mean value of the matrix
e=np.linalg.norm(a)#calculates the norm value of the matrix
f=a/e#normalised matrix by dividing matrix by norm value
g=f.flatten()#flattens the normalised matrix to a 1-D array
h=np.sort(g, axis=0)#sorts the !-D array in increasing order

print()
print("Maximum value of the array is : \n" + str(b))
print()
print("Minimum value of the array is : \n" + str(c))
print()
print("Mean value of the array is : \n" + str(d))
print()
print("Normalised values of array is : \n")
print(f)
print()
print("The normalised array after being flattened is : \n")
print(g)
print()
print("The flattened array after being sorted is : \n")
print(h)

