from day_15_part_1_2 import find_short

file_input = open("day-15-input.txt", "r")
# file_input = open("day-15-test.txt", "r")

_mapp = []
for i in file_input:
    a = [int(_) for _ in i.strip()]
    _mapp.append(a)
    # print(a)        
file_input.close()

def make_new_mapp(mapp):
    new_mapp = []

    for i in range(5*len(mapp)):
        a = []
        for j in range(5*len(mapp[0])):
            no = (mapp[i%len(mapp)][j%len(mapp[0])] + (i//(len(mapp))) + (j//(len(mapp[0]))))
            if no > 9:
                no = no - 9
            a.append(no)
        new_mapp.append(a)

    print("length :", len(new_mapp))
    print("breadth :", len(new_mapp[0]))
    s = ""
    for _ in range(len(new_mapp)):
        s = ""
        # print([_ for _ in new_mapp[_]])
        # for c in range(len(new_mapp)):
        #     s += str(new_mapp[_][c])
        # print(s)
    return new_mapp

if __name__ == "__main__":
    n_mapp = make_new_mapp(_mapp)
    find_short(n_mapp)