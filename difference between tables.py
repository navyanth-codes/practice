# Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2.

# example : 
# Input:
# n1 = 9, n2 = 4
# Output:
# 5 10 15 20 25 30 35 40 45 50 

def difference(n1,n2):
    
    #Complete the code below
    for i in range(1 ,11 ):
        print((n1-n2)*i,end=' ')