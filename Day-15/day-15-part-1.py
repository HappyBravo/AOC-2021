file_input = open("day-15-input.txt", "r")

# file_input = open("day-15-test.txt", "r")
mapp = []
for i in file_input:
    a = [int(_) for _ in i.strip()]
    mapp.append(a)
    # print(a)        
file_input.close()

start = (0, 0) # y, x
end = (len(mapp)-1, len(mapp[len(mapp)-1])-1) # y, x

# print(start, end)
def dist(position):
    y, x = position
    y_end, x_end = end
    d = ((y_end-y)**2 + (x_end - x)**2)**(0.5)
    return d

def find_next(now, times):
    if times < 10: # for weighting purpose or foresighting risks
        times += 1
        y ,x = now
        if (y,x) == end:
            return now
        right = 10000
        down = 10000
        if y<len(mapp)-1:
            down = mapp[y+1][x]*dist((y+1, x)) #+ dist((y+1, x))
            y_, x_ = find_next((y+1, x), times)
            down += mapp[y_][x_]*dist((y_,x_))# + dist((y_,x_))

        if x<len(mapp[len(mapp)-1])-1:
            right = mapp[y][x+1]*dist((y,x+1)) #+ dist((y,x+1))
            y_, x_ = find_next((y, x+1), times)
            right += mapp[y_][x_]*dist((y_,x_)) #+ dist((y_,x_))
        
        if down<right:
            # print("Down -",mapp[y+1][x])
            return (y+1, x) # down
        elif right<down:
            # print("Right -",mapp[y][x+1])
            return (y, x+1) # right
        elif right == down:
            # print("Both equal - ")
            if x<len(mapp[len(mapp)-1])-1:
                y_, x_ = find_next((y, x+1), times)
                level2_right = mapp[y_][x_]*dist((y_,x_)) #+ dist((y_,x_))
            if y<len(mapp)-1:
                y_, x_ = find_next((y+1, x), times)
                level2_down = mapp[y_][x_]*dist((y_,x_)) #+ dist((y_,x_))
            if level2_right < level2_down:
                return (y, x+1)
            else:
                return (y+1, x)
    else:
        return now
summ = 0
res_y , res_x =(0, 0)

def update_mapp(pos):
    _y, _x = pos
    _mapp = [_ for _ in mapp]
    # print(_mapp)
    _mapp[_y][_x] = " "
    s = ""
    for i in range(len(_mapp)):
        print([str(_) for _ in _mapp[i]])
        # s = ",".join(list(map(str, _mapp[i])))
        # s += "\n"
    # return s
    #     for j in range(len(_mapp[i])):
    #         if (i,j) == pos:
    #             _mapp[i][j] = " "            
                
while True:
    # cy, cx = list(map(int, input("Enter y, x : ").split()))
    res_y, res_x = find_next((res_y, res_x), 0)
    summ += mapp[res_y][res_x]
    print(res_y, res_x)
    # update_mapp((res_y, res_x))
    # choice = input("exit ? (y/n) :")
    # if choice == 'y' or (res_y, res_x) == (9,9):
    #     break
    if (res_y, res_x) == end:
        break

print(summ)
