input_file = open("day-1-input.txt", "r")
count = 0
arr = input_file.readlines()
#arr = [199,200,208,210,200,207,240,269,260,263] #given example
input_file.close()
#suffix = "decreased"
print("Total inputs = ", len(arr))
'''
print(arr[0], type(arr[0]))
print(arr[1], type(arr[1]))
print(arr[1]<arr[0])
'''
for i in range(1,len(arr)):
    print("Checking =", arr[i])
    print("count =", count)
    if int(arr[i-1]) < int(arr[i]):
        count+=1
        #suffix = "increased"
    #print("{0} - {1}\t".format(arr[i], suffix), end="")
    #if (i%10 == 0):
    #    print()
print("\nGreater than previous = ", count)