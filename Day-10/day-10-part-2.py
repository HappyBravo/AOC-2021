from statistics import median

file_input = open("day-10-input.txt", "r")
# file_input = open("day-10-test.txt", "r")
# arr = [_ for _ in file_input.readline().strip()]
# print(arr)
# print(len(arr))
'''
bracket = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
            ">" : "<"
            }
open_list = ["[","{","(","<"]
close_list = ["]","}",")",">"]
rate = {")" : 1,"]" : 2, "}" : 3, ">" : 4}

def check(myStr):
    stack = []
    unexp = ""
    temp = ""
    flag = False

    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                print(stack)
                stack.pop()
            else:
                unexp += i
                flag = True
                return ["".join(stack[::-1]), flag]
    if len(stack) > 0:
        s = "".join(stack)
        for _ in s:
            pos = open_list.index(_)
            unexp += close_list[pos]
        unexp = unexp[::-1]
        return [unexp, flag]
    else:
        return [unexp, flag]
    

summ = 0
count = 0
res = []
res_summ = []
for i in file_input:
    # arr = [_ for _ in i.strip()]
    arr = i.strip()
    res_s = check(arr)
    print(res_s)
    flag = res_s[1]
    if not flag:
        res.append(res_s[0])

    # print(res)
    if flag:
        count += 1
    # print(list(rate.keys()))
    #if len(res_s[0]) > 1:
     #   break
print(res)
for line in res:
    summ = 0
    for _ in line:
        if _ in list(rate.keys()) :
            summ = count*summ + rate[_]
    res_summ.append(summ)
file_input.close()

for i in range(len(res)):
    print("{} : {}".format(res[i], res_summ[i]))
result = sorted(set(res_summ))
print(median(result))
# print(result[int((len(result)+1)/2)])
'''
content = file_input
ends = {']': '[', ')': '(', '}': '{', '>': '<'}
scores = []
for line in [l.strip() for l in content]:
    blocks = []
    err = False
    for char in line:
        if char in ends.values():
            blocks.append(char)
        elif char in ends.keys():
            if blocks[-1] == ends[char]:
                print(blocks)
                blocks.pop()
            else:
                err = True
                break
    if not err:
        score = 0
        blocks.reverse()
        for b in blocks:
            score *= 5
            score += {'(': 1, '[': 2, '{': 3, '<': 4}[b]
        scores.append(score)
print(median(scores))
