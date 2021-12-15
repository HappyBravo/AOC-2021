file_input = open("day-15-input.txt", "r")

# file_input = open("day-15-test.txt", "r")
_mapp = []
for i in file_input:
    a = [int(_) for _ in i.strip()]
    _mapp.append(a)
    # print(a)        
file_input.close()


def find_short(mapp):
    start = (0, 0) # y, x
    end = (len(mapp)-1, len(mapp[0])-1) # y, x

    # print(start, end)
    neww = []
    for i in range(len(mapp)):
        arr = []
        for j in range(len(mapp[0])):
            arr.append(0)
        neww.append(arr)
    # print("new arr\n", neww)
    neww[0][0] = mapp[0][0]

    # visited = []

    for i in range(1, len(mapp)):
        neww[i][0] = mapp[i][0] + neww[i-1][0]

    for j in range(1, len(mapp[0])):
        neww[0][j] = mapp[0][j] + neww[0][j-1]

    # print(mapp)
    # print(neww)

    for i in range(1, len(mapp)):
        for j in range(1, len(mapp[0])):
            neww[i][j] = mapp[i][j] + min(neww[i-1][j], neww[i][j-1])

    # for i in range(len(mapp)):
    #     print([_ for _ in neww[i]])
    
    print(neww[0][0], neww[-1][-1])
    print("Ans = ", neww[-1][-1]-neww[0][0])

if __name__ =="__main__":
    find_short(_mapp)