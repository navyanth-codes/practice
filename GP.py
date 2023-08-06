# Given three integer, a, r and n. Where a is the first term, r is the common ratio of a G.P.  
# Calculate the nth term of GP.  The nth term is given by an= a*rn-1

def utility():
    #The following three lines take the input. Don't change them!
    a=int(input())
    r=int(input())
    n=int(input())
    
    #Complete the code below
    ans = a*(r**(n-1))
    #Complete the code above
    
    #The line below prints the output. Don't change it!
    print(ans)


print(5%20)

str="CFG"
print(not(not(str and "")))
print(oct(23)+oct(23))
print(~(~2))