# Given an integer N find the sum of the first N natural number
def nSum(n):
    
    ans = 0
    
    #Write your code here to calculate and return sum of n number.
    #return n+nSum(n-1)
    for i in range(1,n+1):
        ans+=i
    
    return ans