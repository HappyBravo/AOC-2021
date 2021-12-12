choice = []
dict_of_cards = {}
last_choice = 0

def card_input():
    input_file = open("day-4-input.txt", "r")
    card_no = 0
    values = list(map(int,input_file.readline().split(",")))
    for i in input_file:
        #a = (list(map(int,input_file.readline().split())))
        a = (list(map(int,i.split())))

        if len(a) == 0:
            card_no+=1
            dict_of_cards[card_no] = []
            #print("-----------", card_no)
            continue
        dict_of_cards[card_no].append(a)
        #print(a)
    print("number of cards =", len(dict_of_cards))

    # for l in range(1, len(dict_of_cards)+1):
    #     print("{} -- {}".format(l, dict_of_cards[l]))
    input_file.close()
    return values
choice = card_input()
print(len(choice))

def bingo(updatedcard):
    flag = False
    for i in range(5):
        for j in range(5):
            if updatedcard[i][j] == -1:
                flag = True
            else:
                flag = False
                break
        if flag:
            return ("BINGO", "HORI", i)

    for j in range(5):
        for i in range(5):
            if updatedcard[i][j] == -1:
                flag = True
            else:
                flag = False
                break
        if flag:
            return ("BINGO", "VER", j)

def card_check():
    result = {}
    for i in choice:
        print("------ checking -------", i)
        for card_no in range(1, len(dict_of_cards)+1):
            #print("\n",card_no, end ="")
            for j in range(5):
                for k in range(5):
                    if i == dict_of_cards[card_no][j][k]:
                        dict_of_cards[card_no][j][k] = -1
                        #print("{} \n-> {}".format(card_no, dict_of_cards[card_no]))
        for no in range(1, len(dict_of_cards)+1):
            res = bingo(dict_of_cards[no])
            
            if res != None:
                print(res)
                if res[0] == "BINGO":
                    result[no] = res
        if len(result)>0:
            return (i, result)
last_choice, dict_res = card_check()

print(last_choice, dict_res)
print(dict_of_cards[list(dict_res.keys())[0]])
print(dict_res[list(dict_res.keys())[0]][1])

def final_result(l_choice, d_res):
    prod = 0
    summ = 0
    arr = dict_of_cards[list(d_res.keys())[0]]
    m = d_res[list(d_res.keys())[0]]
    for i in range(5):
        if m[1] == "HORI" and m[2] == i:
            continue
        for j in range(5):
            if m[1]=="VER" and m[2] == j:
                continue
            if arr[i][j] != -1:
                summ+=arr[i][j]
                print(summ, end = " - ")
    prod = l_choice*summ
    return prod

print(final_result(last_choice, dict_res))
#print(dict_of_cards[1][1][1])
