print("Digital Differential Analyser Algorithm \n")

import time 
start_time = time.time()

# Collect the endpoints for the user
x0 = int(input("Enter the value of x0: "))
y0 = int(input("Enter the value of y0: "))
x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))

# Calculate the difference of between the two end points
dy = y1 - y0
dx = x1 - x0

# Calculate the number of steps
if dx > dy:
    steps = dx
else:
    steps = dy

# Increment in x and y coordinate  
x_inc = abs(dx/steps)
y_inc = abs(dy/steps)

# Plot the next point
k = 1
print("\nThe Result is: ")
print('Steps \t x \t y')
while (k <= steps):
    x0 = x0 + x_inc
    y0 = y0 + y_inc
    print(k, '\t', round(x0), '\t', round(y0))
    k = k + 1
    
end_time = time.time()
print("Running Time: ", end_time-start_time)