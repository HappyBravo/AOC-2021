import time
import sys
# file_input = open("day-11-input.txt", "r")
file_input = open("day-11-test.txt", "r")
# file_input = open("day-11-test-2.txt", "r")

arr = []
mapp = []
p = []
count = 0
# arr = [_ for _ in file_input.readline().strip()]
# print(arr)
# print(len(arr))
for i in file_input:
    arr = [int(_) for _ in i.strip()]
    mapp.append(arr)
# print(mapp)
file_input.close()

def printing():
    st = ""
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            # print(mapp[i][j], end = ",")
            st = st + str(mapp[i][j]) + ","
        # print()
        st = st + "\n"
    return st
# mapp = [
#         [1,0,0,0],
#         [0,9,8,1],
#         [0,0,0,9]
#         ]

def check_allflash():
    flag = False
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            if mapp[i][j] != 10:
                return False
                # flag = True
            # else:
            #     flag = False
    # return flag
    return True

def flash(point):#, pointset):
    # print(mapp)

    # nw| n |nw
    # w | X | e
    # sw| s |se
    
    # nw, n, ne, w, e, sw, s, se = 0, 0, 0, 0, 0, 0, 0, 0
    y, x = point[0], point[1]
    # if mapp[y][x] == 10:
    #     mapp[y][x] = 0
    #     flash((y,x))
    
    if y != 0 :
        if (y-1, x) not in p:
            # n =
            mapp[y-1][x]+=1
            if mapp[y-1][x] == 10:
                mapp[y-1][x] = 0
                if (y-1,x) not in p:
                    p.append((y-1,x))
                    #flash((y-1, x))
        if x!=0 and (y-1, x-1) not in p:
            # nw = 
            mapp[y-1][x-1]+=1
            if mapp[y-1][x-1] == 10:
                mapp[y-1][x-1] = 0
                if (y-1,x-1) not in p:
                    p.append((y-1,x-1))
                    #flash((y-1, x-1))
        if x!=len(mapp[y])-1 and (y-1, x+1) not in p :
            # ne = 
            mapp[y-1][x+1]+=1
            if mapp[y-1][x+1] == 10:
                mapp[y-1][x+1] = 0
                if (y-1,x+1) not in p:
                    p.append((y-1,x+1))
                    #flash((y-1, x+1))
    if y != len(mapp)-1 :
        if (y+1, x) not in p:
            # s = 
            mapp[y+1][x]+=1
            if mapp[y+1][x] == 10:
                mapp[y+1][x] = 0
                if (y+1,x) not in p:
                    p.append((y+1,x))
                    #flash((y+1, x))
        if x!=0 and (y+1, x-1) not in p:
            # sw = 
            mapp[y+1][x-1]+=1
            if mapp[y+1][x-1] == 10:
                mapp[y+1][x-1] = 0
                if (y+1,x-1) not in p:
                    p.append((y+1,x-1))
                    #flash((y+1, x-1))
        if x!=len(mapp[y])-1 and (y+1, x+1) not in p:
            # se = 
            mapp[y+1][x+1]+=1
            if mapp[y+1][x+1] == 10:
                mapp[y+1][x+1] = 0
                if (y+1,x+1) not in p:
                    p.append((y+1,x+1))
                    #flash((y+1, x+1))
    if x!=0 and (y, x-1) not in p:
        # w =
        mapp[y][x-1]+=1
        if mapp[y][x-1] == 10:
                mapp[y][x-1] = 0
                if (y,x-1) not in p:
                    p.append((y,x-1))
                    #flash((y, x-1))
    if x!=len(mapp[y])-1 and (y, x+1) not in p:
        #e =
        mapp[y][x+1]+=1
        if mapp[y][x+1] == 10:
                mapp[y][x+1] = 0
                if (y,x+1) not in p:
                    p.append((y,x+1))
                    #flash((y, x+1))
   # scan_flash()
    
def stepup():
    # print(mapp)
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            mapp[i][j]+=1
    #print()

def scan_flash():
    # if scan_flash():
    flag = False
    # print("\tBefore")
    # printing()
    
    i = 0
    j = 0
    for i in range(len(mapp)):
    # while i<len(mapp):
        for j in range(len(mapp[i])):
       # while j < len(mapp[i]):
            if mapp[i][j] == 10:
                mapp[i][j] = 0
                # flash((i,j))
                if (i,j) not in p:
                    p.append((i,j))
                flag = True
    #print(p)
    # p = [_ for _ in p_]
    for _ in p :#range(len(p)):
        # print(len(p))
        # print("=======", _)
        # printing()
        # print("=======")
        #time.sleep(30)
        # input()
        flash(_)
    print("\tafter")
    print(printing())

    # if flag:
    #     scan_flash()
    # else:
    #     return

n= int(input("range : "))
ans = []
for _ in range(n+1):
    count += len(p)
    p = []
    # for i in range(len(mapp)):
    #     for j in range(len(mapp[i])):
    #         print(mapp[i][j], end = ",")
    #     print()
    # print(printing(), end ='\r')

    stepup()
    print(_)
    

    if (check_allflash()):
        # print("- - - - - -")
        # print(_)
        ans.append(_)
        # input()
    # else:
        # print("Skipped")
        # input()
    scan_flash()
    
    print("---")
# print(count)
print(ans)
print("First full flash at :", ans[0]-9)
