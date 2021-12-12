def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return (decimal)

input_file = open("day-3-input.txt", "r")
arr = input_file.readlines()
input_file.close()
gamma = ""
epsilon = ""
zero_count = 0
one_count = 0
for i in range(len(arr[0].strip())):
    zero_count = 0
    one_count = 0
    for j in range(len(arr)):
        if arr[j][i] == '0':
            zero_count += 1
        elif arr[j][i] == '1':
            one_count += 1
    if zero_count>one_count:
        gamma = gamma+"0"
        epsilon = epsilon + "1"
    else :
        gamma = gamma + "1"
        epsilon = epsilon + "0"
print(gamma, epsilon)
decimal_gamma = BinaryToDecimal(gamma)
decimal_episilon = BinaryToDecimal(epsilon)
print(decimal_gamma, decimal_episilon)
print("Power = ", decimal_episilon*decimal_gamma)