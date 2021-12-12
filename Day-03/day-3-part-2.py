def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return (decimal)

def findMaxThing(arr, index):
        zero_count = 0
        one_count = 0
        for j in range(len(arr)):
            if arr[j][index] == '0':
                zero_count += 1
            elif arr[j][index] == '1':
                one_count += 1
        if zero_count>one_count:
            return "0"
        else :
            return "1"

def findMinThing(arr, index):
        zero_count = 0
        one_count = 0
        for j in range(len(arr)):
            if arr[j][index] == '0':
                zero_count += 1
            elif arr[j][index] == '1':
                one_count += 1
        if zero_count>one_count:
            return "1"
        else :
            return "0"

max_thing = ""
min_thing = ""

input_file = open("day-3-input.txt", "r")
arr = input_file.readlines()
input_file.close()

l = len(arr[0].strip())
t_ox_arr = []
t_co_arr = []
ox_arr = [_ for _ in arr]
co_arr = [_ for _ in arr]

for i in range(l):
    print("__________")
    print(i)
    print("len of ox arr", len(ox_arr))
    print("len of co arr", len(co_arr))

    if (len(ox_arr)>1):
        max_thing = findMaxThing(ox_arr, i)
        t_ox_arr = []
        for j in range(len(ox_arr)):
            if max_thing == ox_arr[j][i]:
                t_ox_arr.append(ox_arr[j])
        ox_arr = [_ for _ in t_ox_arr]

    if (len(co_arr)>1):
        min_thing = findMinThing(co_arr, i)
        t_co_arr = []
        for j in range(len(co_arr)):
            if min_thing == co_arr[j][i]:
                t_co_arr.append(co_arr[j])
        co_arr = [_ for _ in t_co_arr]

    if (len(co_arr)<=1 and len(ox_arr)<=1):
        break

print(ox_arr, co_arr)
a = BinaryToDecimal(ox_arr[0].strip())
b = BinaryToDecimal(co_arr[0].strip())
print(a, b)
print(a*b)