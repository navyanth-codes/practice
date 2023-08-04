# Given an integer s. Write a program to print the Inverted "Right angle triangle" wall.
# The length of the perpendicular and base is s. Use double loop.

def invTriangleWall(s):
    
    
    #Complete the given code
    #Replace .... by your own code
    
    for i in range(s):
        for j in range(s-i):
            print("* ",end="")
        print()