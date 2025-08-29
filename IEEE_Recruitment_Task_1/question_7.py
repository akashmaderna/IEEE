import numpy as np, random

m=int(input("enter no. of elements in 1st list : ")) # asks for no. of elements in 1st list
n=int(input("enter no. of elements in 2nd list : ")) # asks for no. of elements in 2nd list

a = np.random.randint(1, 11, m)#generates list with m elements randomly picked between 1 and 10
b = np.random.randint(1, 11, n)#generates list with n elements randomly picked between 1 and 10

print('1st randomly generated list is : ')#prints 1st list
print(a)
print('2nd randomly generated list is : ')#prints 2nd list
print(b)

intersection_list=list()#assigns an empty list to variable 'lis'

for i in range(m):#takes elements from 'a' list to match with list 'b' for common elements
    for j in range(n):
        if a[i] == b[j]:# checks for a common element common for a[i] in all elements of 'b' list
            intersection_list = intersection_list + [int(str(b[j]))]# if common element found, adds it to the intersection list
if len(intersection_list)>0 :# checks if there are any common elements in the end
    editted_list=set(intersection_list)#removes repeated element from the list
    print('The common elements in both the lists are : ')#prints the final common elements list
    print(editted_list)
elif len(intersection_list)==0:#prints there is no common element is there is none
    print('There are no elements in common to both the lists.')
            
    
