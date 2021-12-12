input_file = open("day-1-input.txt", "r")
count = 0
arr = list(map(int, input_file.readlines()))
for i in range(0, len(arr)-3):
    print(i)
    j = i+1
    print(j)
    if sum([arr[i], arr[i+1], arr[i+2]]) < sum([arr[j], arr[j+1], arr[j+2]]):
        count+=1
print(count)