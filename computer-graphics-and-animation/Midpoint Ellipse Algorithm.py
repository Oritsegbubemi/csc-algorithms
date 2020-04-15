print("Midpoint Ellipse Algorithm \n")

import time 
start_time = time.time()
  
def midPointEllipseDraw(rx, ry):  
    x = 0
    y = ry
    xc = 0
    yc = 0
    k = 0
    # Initial decision parameter of region 1  
    p1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x  
    dy = 2 * rx * rx * y  
  
    # For region 1 
    print("K\t Q1(x,y) Q2(-x,y) Q3(x,-y) Q4(-x,-y)")
    while (dx < dy):  
        # Print points based on 4-way symmetry  
        print("K = ", k, "\t(", x + xc, ",", y + yc, ")", sep = "", end = "")
        print("(",-x + xc,",", y + yc, ")", sep = "", end = "")
        print("(",x + xc,",", -y + yc ,")", sep = "", end = "")  
        print("(",-x + xc, ",", -y + yc, ")", sep = "") 
        # Checking and updating value of  
        # decision parameter based on algorithm  
        k += 1
        if (p1 < 0):  
            x += 1;  
            dx = dx + (2 * ry * ry) 
            p1 = p1 + dx + (ry * ry) 
        else: 
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)  
            dy = dy - (2 * rx * rx)  
            p1 = p1 + dx - dy + (ry * ry)  
        
    # Decision parameter of region 2  
    print("-" * 40)
    p2 = (((ry * ry)*((x + 0.5)*(x + 0.5)))+((rx * rx)*((y - 1)*(y - 1)))-(rx * rx * ry * ry))  
  
    # Plotting points of region 2  
    k = 0
    while (y >= 0): 
        # printing points based on 4-way symmetry  
        print("K = ", k, "\t(", x + xc, ",", y + yc, ")", sep = "", end = "")
        print("(",-x + xc,",", y + yc, ")", sep = "", end = "")
        print("(",x + xc,",", -y + yc ,")", sep = "", end = "")  
        print("(",-x + xc, ",", -y + yc, ")", sep = "") 
        # Checking and updating parameter  
        # value based on algorithm  
        k += 1
        if (p2 > 0): 
            y -= 1
            dy = dy - (2 * rx * rx) 
            p2 = p2 + (rx * rx) - dy
        else: 
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            p2 = p2 + dx - dy + (rx * rx)  
  
# MidPoint Ellipse Function Call
midPointEllipseDraw(8, 6);  

end_time = time.time()
print("Running Time: ", end_time-start_time)