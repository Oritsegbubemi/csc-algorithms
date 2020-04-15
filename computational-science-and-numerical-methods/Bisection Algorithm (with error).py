print('Bisection Algorithm - Error')
import math

def f(x):
    fx = math.pow(x,3) - (3 * x) + 1
    return fx

a, b = 0, 1
old_value = a
err = 0.05
abs_err = 1

while(abs_err >= err):
    c = (a+b)/2
    if (f(a)*f(c))<0:
        a, b = a, c
    else:
        a, b = c, b
    abs_err = abs(c - old_value)
    old_value = c

print("The root of the equation is %0.4f"%c)
print("The function of the equation is %0.4f"%f(c))
print("The absolute error of the equation is %0.4f"%abs_err)   