file_input = open("day-8-input.txt", "r")
# file_input = open("day-8-test.txt", "r")
# arr = file_input.readline().split("|")[1].split()
# print(arr)
arr = []
larr = []
output = ""
summ = 0
count =0
one = ""
four = ""
seven = ""
eight = ""
for i in file_input:
    output = ""
    arr, larr = i.split("|")[1].split(), i.split("|")[0].split() 
    #print(["".join(sorted(_)) for _ in arr])
    # print([len(_) for _ in arr])
    for _ in arr + larr:
        if len(_) == 2:
            one = _
        elif len(_) == 4:
            four = _
        elif len(_) == 3:
            seven = _
        elif len(_) == 7:
            eight = _

    for _ in arr:
        if len(_) == 2:
            output += '1'
            count +=1
            # one = _
        elif len(_) == 4:
            output += '4'
            count +=1

        elif len(_) == 3:
            output += '7'
            count +=1

        elif len(_) == 7:
            output += '8'
            count +=1

        elif len(_) == 5:
            if len(set(_) & set(one)) == 2:
                output += '3'
            elif len(set(_) & set(four)) == 3:
                output += '5'
            else:
                output += '2'
        elif len(_) == 6:
            if len(set(_) & set(four)) == 4:
                output += '9'
            elif len(set(_) & set(seven)) == 3:
                output += '0'
            else:
                output += '6'
    summ += int(output)
    print("Output = {}\tsumm = {}".format(output,summ ))
print("\nsumm = {}, [pt1 : count = {}]".format(summ, count))
file_input.close()