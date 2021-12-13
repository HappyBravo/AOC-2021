# file_input = open("day-7-input.txt", "r")
file_input = open("day-7-test.txt", "r")
arr = list(map(int, file_input.readline().split(",")))
file_input.close()

# print(arr)
min_f = -1
min_at = arr[0]
# print(max(arr))
summ = 0
poss_positions = [_ for _ in range(max(arr))]

for i in poss_positions:
    # print("checking", i)
    summ = 0
    for j in arr:
        n = abs(j-i)
        summ += n*(n+1)/2
    if min_f == -1:
        min_f = summ
    elif min_f > summ:
        min_f = summ
        # print("- - - - Min =", i)
        min_at = i
    # print("\tMin = {}, Summ = {}".format(min_f, summ))
print(" -"*22)
print("\t - min at:\t{}\n\t - fuel sum:\t{}".format(min_at, min_f))
print(" -"*22)

