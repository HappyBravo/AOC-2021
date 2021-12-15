from day_15_part_2 import make_new_mapp
import os
import time
import math

clear : lambda : os.system("cls")

file_input = open("day-15-input.txt", "r")
# file_input = open("day-15-test.txt", "r")

_mapp = []
for i in file_input:
    a = [int(_) for _ in i.strip()]
    _mapp.append(a)
    # print(a)        
file_input.close()

new_mapp = make_new_mapp(_mapp)
# new_mapp = _mapp
def neighbors(xy):
    (x, y) = xy
    # return [(x+1, y), (x, y+1)]
    
    #------------------------------------
    #- We can travel in all four directions
    #------------------------------------
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def updated_mapp(gridd, re, counts):
    os.system("cls")
    # print("- - "*22)
    # print("\t\t\t\tIteration :", counts)
    # print("- - "*22)
    st = "\t | "

    for y in range(len(new_mapp)):
        a = []
        for x in range(len(new_mapp[0])):
            if (x,y) in re:
                a.append(" ")
                st+="  "
            else:
                # a.append(str(gridd[(x,y)]))
                a.append("#")
                st+="# "
        st+="| \n\t | "
    print(st)
    print("\n")
    #time.sleep(0.05)
    # input("Enter to continue...")


def traverse_cost(start, end, c):
    steps = 1
    cost = { start: 0 }
    active = set([start])
    visited = set([])
    
    while active:
        steps+=1
        current = min(active, key=cost.get)

        if current == end:
            return cost[current]

        active.remove(current)
        visited.add(current)
        for xy in neighbors(current):
            if xy in c and xy not in active:
                n_cost = cost.get(current, 0) + c[xy]
                if n_cost < cost.get(xy, math.inf):
                    cost[xy] = n_cost
                    active.add(xy)
        print(steps, end="\r")
        # updated_mapp(c, visited, steps)

C = {}
for i in range(len(new_mapp)):
    for j in range(len(new_mapp[0])):
        C[(j, i)] = new_mapp[i][j]

c1 = C
start = (0, 0)
end = (len(new_mapp[0])-1, len(new_mapp)-1)

cos = traverse_cost(start, end, c1)
print("\nAns :",cos)


