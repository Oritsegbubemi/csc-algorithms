with open("Gbubemi_CSC432.txt","w+") as file:
    goal_1 = "To have an A in CSC432"
    goal_2 = "To have an indepth knowledge of this course"
    goal_3 = "To have a stress free time when studying"
    file.write(goal_1)
    file.write("\n"+goal_2)
    file.write("\n"+goal_3)

import os
os.rename("Gbubemi_CSC432.txt","Gbubemi_CSC432_goals.txt")

with open("Gbubemi_CSC432_goals.txt","a+") as file:
    goal_4 = "To be the best student in this course"
    goal_5 = "To do excellently well in my exam"
    file.write("\n"+goal_4)
    file.write("\n"+goal_5)

with open("Gbubemi_CSC432_goals.txt","r") as file:
    goals = file.readlines()
print(goals)
with open("Gbubemi_CSC432_goals.txt","w") as file:
    for goal in goals:
        if goal.strip("\n") != goal_2:
            file.write(goal)
