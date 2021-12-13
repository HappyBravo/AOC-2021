file_input = open("day-10-input.txt", "r")
# file_input = open("day-10-test.txt", "r")
# arr = [_ for _ in file_input.readline().strip()]
# print(arr)
# print(len(arr))
bracket = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
            ">" : "<"
            }
open_list = ["[","{","(","<"]
close_list = ["]","}",")",">"]
rate = {")" : 3,"]" : 57, "}" : 1197, ">" : 25137 }

def check(myStr):
    stack = []
    unexp = ""
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                unexp = i
                return unexp
    if len(stack) == 0:
        return "Balanced"
    else:
        return unexp

summ = 0
for i in file_input:
    # arr = [_ for _ in i.strip()]
    arr = i.strip()
    res = check(arr)
    print(res)
    # print(list(rate.keys()))
    if res in list(rate.keys()) :
        summ += rate[res]
file_input.close()
print(summ)