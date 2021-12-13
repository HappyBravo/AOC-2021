file_input = open("day-9-input.txt", "r")
# file_input = open("day-9-test.txt", "r")
h_map = []
for i in file_input:
    arr = [int(_) for _ in i.strip()]
    h_map.append(arr)
file_input.close()
# print(h_map)
# print(len(h_map))
file_input.close()
dict_basin ={}

def find_basin(sink, points):
    y, x = points[0], points[1]
    up = 9
    down = 9
    right = 9
    left = 9
    # num = h_map[sink[0]][sink[1]]
    # print(num)
    if y != 0 :
        up = h_map[y-1][x]
        #print(up)
        if up<9 and (y-1, x) not in dict_basin[(sink[0], sink[1])]:
            dict_basin[(sink[0], sink[1])].append((y-1, x))
            # find_basin(sink, (y-1, x))
    if y != len(h_map)-1:
        down = h_map[y+1][x]
        #print(down)

        if down<9 and (y+1, x) not in dict_basin[(sink[0], sink[1])]:
            dict_basin[(sink[0], sink[1])].append((y+1, x))
            # find_basin(sink, (y+1, x))

    if x != 0:
        left = h_map[y][x-1]
        #print(left)

        if left<9 and (y, x-1) not in dict_basin[(sink[0], sink[1])]:
            dict_basin[(sink[0], sink[1])].append((y, x-1))
            # find_basin(sink, (y, x-1))

    if x != len(h_map[y])-1:
        right = h_map[y][x+1]
        #print(right)

        if right<9 and (y, x+1) not in dict_basin[(sink[0], sink[1])]:
            dict_basin[(sink[0], sink[1])].append((y, x+1))
            # ind_basin(sink, (y, x+1))
    # if ((num < up) and (num < down) and (num < right) and (num < left)):
    #         # print(" - - - - ", up, down, right, left, num)
    #         dict_basin[(sink[0], sink[1])].append()

    # print(dict_basin)
    



def check_basin(sink):
    #print(h_map)
    y, x = sink[0], sink[1]
    dict_basin[(y,x)] = [(y,x)]
    count = 0
    while count < len(set(dict_basin[(y,x)])):
        find_basin(sink, dict_basin[(y,x)][count])
        count += 1
    
    


        

# check_basin((0,9))
# print(dict_basin)
# print(len(dict_basin[(0,9)]))

num = 0
lower_arr = []
for i in range(len(h_map)):
    for j in range(len(h_map[i])):
        up = 9
        down = 9
        right = 9
        left = 9
        num = h_map[i][j]
        print(num, end = "")
        # if num<9:
        #     print(".", end= "")
        # else:
        #     print("|", end="")

        if i != 0 :
            up = h_map[i-1][j]
        if i != len(h_map)-1:
            down = h_map[i+1][j]
        if j != 0:
            left = h_map[i][j-1]
        if j != len(h_map[i])-1:
            right = h_map[i][j+1]
        if ((num < up) and (num < down) and (num < right) and (num < left)):
            # print(" - - - - ", up, down, right, left, num)
            lower_arr.append((i,j))  
    # print("---"*10)
    print()
    # print(h_map[i])
# print(lower_arr)
# ans = sum(lower_arr)+(len(lower_arr))
# print(ans)
size_arr = []
for sink_ponits in lower_arr:
    check_basin(sink_ponits)
    print("{} :- - - size = {}".format(sink_ponits, len(dict_basin[sink_ponits])))
    size_arr.append(len(dict_basin[sink_ponits]))
print(size_arr)
print(sorted(set(size_arr)))
ans = sorted(set(size_arr))[-1:-4:-1]
a = 1
for i in range(3):
    a *= ans[i]
print(a)