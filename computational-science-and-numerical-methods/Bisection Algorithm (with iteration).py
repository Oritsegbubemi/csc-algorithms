print('Bisection Algorithm - Iteration')
import math

def f(x):
    fx = math.pow(x,3) - (3 * x) + 1
    return fx

a, b = 0, 1
old_value = a
k =1 

while(k <= 5):
    c = (a+b)/2
    if (f(a)*f(c))<0:
        a, b = a, c
    else:
        a, b = c, b
    k = k + 1

print("The root of the equation is %0.4f"%c)
print("The function of the equation is %0.4f"%f(c))
