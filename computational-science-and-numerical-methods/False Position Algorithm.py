print("False Position Algorithm")

def f(x):
    fx = pow(x,3) + x + 1
    return fx

# Initailze Variables
a, b = -1, -0.5
k = 1

# Loop using a set number of iteration
while(k <= 15):
    c = b - ((f(b) * (a-b)) / (f(a) -f(b)))
    print(k,"\t", a,"\t", b,"\t", f(a),"\t", f(b),"\t", c,"\t",f(c))
    if (f(a)*f(c)) < 0:
        a, b = a, c
    else: 
        a, b = c, b  
    k = k + 1
   
"""
# Loop using error
old_value = a
err = 0.0001
abs_err = 1
while(abs_err > err):
    c = b - ((f(b) * (a-b)) / (f(a) -f(b)))
    print(k,"\t", a,"\t", b,"\t", f(a),"\t", f(b),"\t", c,"\t", f(c),"\t", abs_err)
    if (f(a)*f(c)) < 0:
        a, b = a, c
    else: 
        a, b = c, b  
    abs_err = abs(c - old_value)
    old_value = c
    k = k + 1
"""