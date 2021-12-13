file_input = open("day-13-input.txt", "r")
# file_input = open("day-13-test.txt", "r")

dot_map = []
folds = []
flag = False
max_x = 0
max_y = 0

for i in file_input:
    if flag:
        arr = i.strip().split()[-1].split("=")
        # print(arr)
        folds.append((arr[0], int(arr[1])))
        # print((arr[0], int(arr[1])))
    # print(i.strip())
    elif len(i.strip()) == 0:
        # print("empty")
        flag = True
    else:
        arr = tuple(map(int, i.strip().split(",")))
        # print(arr)
        if max_x < arr[0]:
            max_x = arr[0]

        if max_y < arr[1]:
            max_y = arr[1]
        dot_map.append(arr)

file_input.close()
print("x -", max_x)
print("y -", max_y)

def print_map():
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in dot_map:
                print("#", end="")
            else:
                print(".", end="")
        print()

# print("Before\n", dot_map)
# print_map()
print(len(dot_map))

# print(folds)

inst = folds[0]
direction, coor = inst
# print(direction, coor)
for i in range(len(dot_map)):
    x, y = dot_map[i]
    if direction == 'y':
        max_y = coor
        if y>coor:
            y = (coor*2) - y
    # dot_map[i] = (x, y)
    elif direction == 'x':
        max_x = coor
        if x>coor:
            x = (coor*2) - x
    dot_map[i] = (x, y)
dot_map = list(set(dot_map))
# print("\nAfter\n", dot_map)
# print_map()
print(len(dot_map))