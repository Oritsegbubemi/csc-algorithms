print("Bresenham Algorithm\n")

import time 
start_time = time.time()

# Collect the endpoints for the user
x0 = int(input("Enter the value of x0: "))
y0 = int(input("Enter the value of y0: "))
x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))

# Find the Slope
dy = y1 - y0
dx = x1 - x0
slope = dy/dx
pk = 0

# Initial Iteration
if slope < 1:
    pk = (2 * dy) - dx
    if pk >= 0:
        x_new = x0 + 1
        y_new = y0 + 1
    elif pk < 0:
        x_new = x0 + 1
        y_new = y0
elif slope > 1:
    pk = (2 * dx) - dy
    if pk >= 0 :
        x_new = x0 + 1
        y_new = y0 + 1
    elif pk < 0:
        x_new = x0
        y_new = y0 + 1
print('Pk \t x \t y')
print(pk, '\t', x_new, '\t', y_new)

# Other Iteration
while (x_new != x1 or y_new != y1):
    if slope < 1:
        pk = pk + (2 * dy) - (2 * dx * (y_new - y0))
        y0 = y_new
        if pk >= 0:
            x_new = x0 + 1
            y_new = y0 + 1
        elif pk < 0:
            x_new = x0 + 1
            y_new = y0     
    elif slope > 1:
        pk = pk + (2 * dx) - (2 * dy * (x_new - x0))
        x0 = x_new
        y0 = y_new
        if pk >= 0:
            x_new = x0 + 1
            y_new = y0 + 1
        elif pk < 0:
            x_new = x0
            y_new = y0 + 1
    print(pk, '\t', x_new, '\t', y_new)

end_time = time.time()

print("Running Time: ", end_time-start_time)
