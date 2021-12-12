input_file = open("day-2-input.txt", "r")
arr = input_file.readlines()
input_file.close()
#arr = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]
command = []
x = 0
y = 0
aim = 0
for i in range(len(arr)):
    command = arr[i].split()
    if command[0] == "forward":
        x = x+int(command[1])
        y = y-aim*int(command[1])
    elif command[0] == "down":
        #y = y-int(command[1])
        aim = aim+int(command[1])
    elif command[0] == "up":
        #y = y+int(command[1])
        aim = aim-int(command[1])
    #print(x,y,aim)
print(x)
print(y)
print(x*(-y))