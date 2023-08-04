# Given an integer N. Write a program to print all the divisors of N
def divisor(n):
    
    # Complete the code given below
    #Replace .... with your own code
    
    for i in range(1,n+1):
        if n%i==0 :
            print(i, end = ' ')