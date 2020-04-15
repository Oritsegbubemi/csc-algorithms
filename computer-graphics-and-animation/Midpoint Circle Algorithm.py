print("Midpoint Circle Algorithm \n")

import time 
start_time = time.time()

def midPointCircleDraw(r): 
    x = 0
    y = r
    x_center = 0
    y_center = 0
    k = 0
    # Initialising the value of P 
    P = 1 - r 
    print("K\t Q1(x,y) Q2(-x,y) Q3(x,-y) Q4(-x,-y)")
    
    # For the first half of the quarter
    while (x < y): 
        print("K = ", k, "\t(", x + x_center, ", ", y + y_center, ")", sep = "", end = "")  
        print("(", -x + x_center, ", ", y + y_center, ")", sep = "", end = "")  
        print("(", x + x_center, ", ", -y + y_center, ")", sep = "", end = "")  
        print("(", -x + x_center, ", ", -y + y_center,")", sep = "") 
        k += 1
        x += 1 
        if (P >= 0): 
            yk = y
            y -= 1
            P = P + (2 * x) + (pow(y,2)- pow(yk,2)) - (y - yk) + 1 
        else: 
            P = P + (2 * x) + 1 
    print("-" * 40)
    
    # For the second half of the quarter
    while (y >= 0):
        print("K = ", k,"\t(", x + x_center, ", ", y + y_center, ")", sep = "", end = "")  
        print("(", -x + x_center, ", ", y + y_center, ")", sep = "", end = "")  
        print("(", x + x_center, ", ", -y + y_center, ")", sep = "", end = "")  
        print("(", -x + x_center, ", ", -y + y_center,")", sep = "") 
        k += 1
        y -= 1
        if (P >= 0):
            xk = x - 1
            x = x + 1
            P = P + (2 * y) + (pow(xk,2)- pow(x,2)) - (xk - x) - 1 
        else:
            P = P + (2 * x) - 1
            
# MidPoint Circle Function Call
midPointCircleDraw(8) 

end_time = time.time()
print("Running Time: ", end_time-start_time)