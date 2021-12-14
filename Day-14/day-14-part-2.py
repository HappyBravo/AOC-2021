file_input = open("day-14-input.txt", "r")
# file_input = open("day-14-test.txt", "r")

template = ""
lib = {}
flag = False

for i in file_input:
    if flag:
        arr = i.strip().split(" -> ")
        # print(arr)
        if arr[0] in lib:
            lib[arr[0]].append(arr[1])
        else:
            lib[arr[0]] = arr[1]
    elif len(i.strip()) == 0:
        # print("empty")
        flag = True
    else:
        template = i.strip()
        
file_input.close()

# print(template)
# print(lib)
# print(len(lib))
# temp = ""
# count = 0
element_count = {}
code_count = {}

n = int(input("Enter no of steps : "))
# while True:

for ele in template:
    if ele in element_count:
        element_count[ele] += 1
    else:
        element_count[ele] = 1

for i in range(len(template)-1):
    code = template[i:i+2]
    if code in code_count:
        code_count[code] += 1
    else:
        code_count[code] = 1
print(code_count)

iter = 0
while iter<n:
    '''
    temp = ""
    for i in range(len(template)):
        code = template[i:i+2]
        if code in lib:
            temp += template[i:i+1]+lib[code]
        else:
            temp += template[i:i+1]
    template = temp
    print(template)
    # d = input("Exit ?")
    # if d == "y":
    #     break
    '''
    # pair
    print(element_count)
    for code, count in code_count.copy().items():
        #if code in lib:
        new_ele = lib[code]	# AC -> B
        if new_ele in element_count:
            element_count[new_ele] += count	# add B
        else:
            element_count[new_ele] = 1
        code_count[code] -= count	# AC -> ABC, AC pair is gone
        if code[0] + new_ele in code_count:
            code_count[code[0] + new_ele] += count	# AB from ABC
        else:
            code_count[code[0] + new_ele] = count
        if new_ele + code[1] in code_count:
            code_count[new_ele + code[1]] += count	# BC from ABC
        else:
            code_count[new_ele + code[1]] = count
    iter += 1
'''
for _ in template:
    if _ in element_count:
        element_count[_]+=1
    else:
        element_count[_] = 1
'''
print(element_count)

val_list = sorted(list(element_count.values()))
print(val_list[-1] - val_list[0])