file_input = open("day-5-input.txt", "r")
#file_input = open("day-5-test.txt", "r")

# a = [tuple(map(int, i.split(","))) for i in file_input.readline().split("->")]
# print(a)
arr = []
for i in file_input:
    coordinate = [tuple(map(int, _.split(","))) for _ in i.split("->")]
    #print(coordinate)
    if ((coordinate[0][0] == coordinate[1][0]) or (coordinate[0][1] == coordinate[1][1])):
        arr.append(coordinate)
print(len(arr))
#print(arr)
#print(arr[-1])
file_input.close()

vent_map = {}
for i in (arr):
    print(i)
    x0 = i[0][0]
    y0 = i[0][1]
    x1 = i[1][0]
    y1 = i[1][1]
    x = x0
    y = y0
    if x0 == x1:
        #print(x, y)
        #print("enter loop")
        inc = 1
        if y1<y0:
            inc = -1
        for y in range(y0, y1+inc, inc):
            #print(x,y)
            try:
                vent_map[(x, y)] += 1
            except:
                vent_map[(x, y)] = 1
    else:
        #print(x, y)
        #print("enter loop")
        inc = 1
        if x1<x0:
            inc = -1
        for x in range(x0, x1+inc, inc):
            #print(x,y)
            try:
                vent_map[(x, y)] += 1
            except:
                vent_map[(x, y)] = 1
#print(vent_map)
print(len(vent_map), (len(vent_map))**0.5)
print(len([i for i in vent_map if vent_map[i] > 1]))