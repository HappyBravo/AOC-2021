file_input = open("day-8-input.txt", "r")
# file_input = open("day-8-test.txt", "r")
# arr = file_input.readline().split("|")[1].split()
# print(arr)
arr = []
count = 0
for i in file_input:
    arr = i.split("|")[1].split()
    lengths = [len(_) for _ in arr]
    for j in lengths:
        if j in [7, 3, 2, 4]:
            '''
            digit 8 : 7
            digit 4 : 4
            digit 1 : 2
            digit 7 : 3
            '''
            count +=1
            
print(count)
file_input.close()