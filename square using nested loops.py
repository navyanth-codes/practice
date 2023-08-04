# Given an integer s,  write a program to print a square wall of size s without using string multiplication.
# Use nested loops instead. The * character will make up the wall.
def squareWall(s):
    
    #Complete the codes below 
    #Replace .... with your own code
    for i in range(s):
        
        for j in range(s):
            print("* ",end="")
        #This print below gives new line, so you don't have to.
        print()