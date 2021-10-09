from math import sqrt

while True:     #Checks for integer input
    try:
        n = int(input('Please enter an integer: ')) #get integer
        break
    except ValueError:  #If not integer
        print('Integers only please.')
        continue

if n > 1:   #Checks for input of 1
    for i in range(2, int(sqrt(n))+1):  #Checks from 2 to sqrt(n)
        if (n % i == 0):                #If number n is evenly divisible by a number, print is not prime
            print (n, "is not prime")
            break
    else:                               #If number n is not evenly divisible by any numbers, print is prime
        print(n, 'is prime')
else:                                   #One is not prime
    print(n, 'is not prime')


#We can check until sqrt(n) because any larger numbers are made up of the smaller factors that have already been checked