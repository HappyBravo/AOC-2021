import math
file_input = open("day-17-input.txt", "r")

# file_input = open("day-17-test.txt", "r")

target_x_range = []
target_y_range = []

for i in file_input:
    a = i.strip().split()
    # print(a)
    x = list(map(int, a[2][:-1].split("=")[-1].split("..")))
    y = list(map(int, a[3].split("=")[-1].split("..")))
    # print(x,y)
    target_x_range = x
    target_y_range = y
file_input.close()

print(target_x_range, target_y_range)

vel_y0_max = max([abs(_) for _ in target_y_range])-1
vel_x0_max = max([abs(_) for _ in target_x_range])
vel_x0_min = round((-1 + math.sqrt(1 + (8*target_x_range[0])))/2)
print("vel x_min :", vel_x0_min)
print("vel x_max :", vel_x0_max)
print("vel y_max :", vel_y0_max)



points_in_target = []
path_points = {}

def add_target_points(x_range, y_range):
    for i in range(y_range[0], y_range[1]+1):
        for j in range(x_range[0], x_range[1]+1):
            points_in_target.append((j,i))
            # print((j,i), end=",")
            # print("T", end = " ")
        # print()
print("---"*3)

add_target_points(target_x_range, target_y_range)


# y_coo = [_ for _ in range(y_stretch[0], y_stretch[1]+1)]
# if y_stretch[0] < 0:
def print_region(x_range, y_range, _path_points = []):
    if len(points_in_target) == 0:
        add_target_points(x_range, y_range)

    x_stretch = [min([0]+x_range), max([0]+x_range)]
    y_stretch = [min([0]+y_range), max([0]+y_range)]
    print(x_stretch)
    print(y_stretch)
    i = 0
    i_min = y_stretch[0]
    i_max = y_stretch[1]
    i = i_max
    while i>=i_min:
        s = "."
        for j in range(x_stretch[0], x_stretch[1]+1): # assumption: particle goes in +ve x direction always
            # s = "."
            if (j,i) in points_in_target:
                s = "T"
                # print("T", end="")
            if (j,i) in _path_points:
                s = "#"
            # else:
            #     s = "."
            print(s, end="")
        print()
        i -= 1

# print_region(target_x_range, target_y_range)

def distance_covered(initial_speed):
    # a = -1
    d = 0
    # d = (initial_speed/2)*(2*initial_speed + (initial_speed -1)*a)
    d = initial_speed*(initial_speed + 1)*0.5
    return int(d)

print(distance_covered(vel_y0_max))

def analyse_velocity(v_x, v_y):
    # drag = -1
    # gravity = -1
    vx = v_x
    vy = v_y
    x = 0
    y = 0
    ppath = []
    while x <= max(target_x_range) and y >= min(target_y_range):
        x += v_x
        y += v_y
        # print(x, y, end = "")
        if v_x > 0:
            v_x = v_x -1
        v_y = v_y - 1
        ppath.append((x,y))
        # print(ppath)

        if (x,y) in points_in_target:
            # input()    
            return ppath
    # nput()
    return ppath


# start = (0, 0)
x_pos, y_pos = (0, 0)
temp = []
for v_x in range(vel_x0_min, vel_x0_max+1):
    temp = []
    # x = 0
    # y = 0
    for v_y in range(-vel_y0_max-1, vel_y0_max+1):
       # 
       # print(v_x, v_y, end=", ")
       temp = analyse_velocity(v_x, v_y)
       a = []
       for idx in range(len(temp)):
           if temp[idx] in points_in_target:
               path_points[(v_x, v_y)] = temp

    # print_region(())
    # print()

print(list(path_points.keys()))
print(len(path_points))