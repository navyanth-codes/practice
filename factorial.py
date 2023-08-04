# Given an integer N. Write a program to return the factorial of N.
def nFactorial(n):
    
    ans = 1
    
    
    #Write your code below
    # for i in range(n):
    #     ans*=i
    
    # while(n>0):
    #     ans*=n
        
    if(n in(0,1)):
        return 1
    else:
        return n*nFactorial(n-1)
    
    return ans