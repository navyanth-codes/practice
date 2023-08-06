# You are given two integer variables x and y. You need to perform the following operations:

# p = x+y : Addition
# q = x-y : Subtraction
# r = x*y :Multiplication
# s = x/y : Float Division with a precision of 5 decimal places
# t = x//y : Int Division
# u = x%y : Modulo
# v = x**y : Power

def utility():
    
    x=int(input())
    y=int(input())
    
    # Perform addition x+y below
    p = x+y
    # Perform subtraction x-y below
    q = x-y
    # Perform multiplication x*y below
    r = x*y
    # Perform float division x/y below
    s = x/y
    # Perform integer divison x//y below
    t = x//y
    # Perform modulo operation x%y below
    u = x%y
    # Perform power(x,y) x**y below
    v = x**y
    
    
    print(p,q,r,"{:.5f}".format(s),t,u,v)