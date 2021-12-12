file_input = open("day-5-input.txt", "r")
# file_input = open("day-5-test.txt", "r")

# a = [tuple(map(int, i.split(","))) for i in file_input.readline().split("->")]
# print(a)
arr = []
for i in file_input:
    coordinate = [tuple(map(int, _.split(","))) for _ in i.split("->")]
    #print(coordinate)
    #if ((coordinate[0][0] == coordinate[1][0]) or (coordinate[0][1] == coordinate[1][1])):
    arr.append(coordinate)
print(len(arr))
#print(arr)
#print(arr[-1])
file_input.close()

vent_map = {}
for i in (arr):
    #print(i)
    x0 = i[0][0]
    y0 = i[0][1]
    x1 = i[1][0]
    y1 = i[1][1]
    x = x0
    y = y0
    x_count = 0
    y_count = 0
    
    x_inc = 1
    y_inc = 1
    
    if x1<x0:
        x_inc = -1
    elif x1==x0:
        x_inc = 0

    if y1<y0:
        y_inc = -1
    elif y1==y0:
        y_inc = 0
    
    while True:
        if ((x_count > abs(x0-x1)) and (x_inc !=0)): 
            break
        if ((y_count > abs(y0-y1)) and (y_inc != 0)):
            break

        #print("\t checking", (x,y))
        try:
            #print("Try")
            vent_map[(x, y)] += 1
        except:
            #print("Except")
            vent_map[(x, y)] = 1
        #print("-")
        y += y_inc
        x += x_inc
        x_count +=1
        y_count +=1
    
#print(vent_map)
print(len(vent_map))#, (len(vent_map))**0.5)
print(len([i for i in vent_map if vent_map[i] > 1]))