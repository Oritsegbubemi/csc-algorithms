print("Newton Algorithm")

def f(x): 
    fx = pow(x, 3) - (2 * x * x) + x -3
    return fx

def g(x):
    gx = (3 *(pow(x, 2))) - (4 * x) + 1
    return gx

n = 1
x0 = 4

while (n<=4):
    c = x0 - (f(x0)/g(x0))
    n = n + 1
    x0 = c 
print("The root is %.4f"%c)
    
    
