n = int(input('Enter value of n : '))#asks for value of n

for i in range(1,n+1):#prints stars from 1 to n by multiplying single star starting from 1 to n times
    print(" "*(n-i) + "*"*i)#since stars are on left, so total spaces before stars will be n-i, where i ranges from 1 to n

    
