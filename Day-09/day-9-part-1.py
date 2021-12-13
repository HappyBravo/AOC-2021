# file_input = open("day-9-input.txt", "r")
file_input = open("day-9-test.txt", "r")
# arr = [_ for _ in file_input.readline().strip()]
# print(arr)
# print(len(arr))
h_map = []
for i in file_input:
    arr = [int(_) for _ in i.strip()]
    h_map.append(arr)
file_input.close()
# print(h_map)
# print(len(h_map))
# up = 10
# down = 10
# right = 10
# left = 10
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
            lower_arr.append(num)  
    # print("---"*10)
    print()
    # print(h_map[i])
print(lower_arr)
ans = sum(lower_arr)+(len(lower_arr))
print(ans)