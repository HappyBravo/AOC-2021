# file_input = open("day-14-input.txt", "r")
file_input = open("day-14-test.txt", "r")

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
temp = ""
count = 0
n = int(input("Enter no of steps : "))
# while True:
while count<n:
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
    count += 1
element_count = {}
for _ in template:
    if _ in element_count:
        element_count[_]+=1
    else:
        element_count[_] = 1
print(element_count)

val_list = sorted(list(element_count.values()))
print(val_list[-1] - val_list[0])