print("Secant Algorithm")

def f(x):
    fx = pow(x, 5) + pow(x, 3) + 3
    return fx

x0 = -1
x1 = -1.1
err = 0.0001
abs_err = abs(x1 - x0)
k = 1

while (abs_err >= err):
    new_value = x1 - ((f(x1) * (x1 - x0))/(f(x1)-f(x0)))
    print(k, "\t", x0, "\t", f(x0), "\t", x1, "\t", abs_err)
    abs_err = abs(new_value - x1)
    x0 = x1
    x1 = new_value
    k = k + 1