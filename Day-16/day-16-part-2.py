import math
file_input = open("day-16-input.txt", "r")

file_input = open("day-16-test.txt", "r")
# file_input = open("day-16-test-2.txt", "r")
# file_input = open("day-16-test-3.txt", "r")
# file_input = open("day-16-test-4.txt", "r")
# file_input = open("day-16-test-5.txt", "r")
# file_input = open("day-16-test-6.txt", "r")
# file_input = open("day-16-test-7.txt", "r")

decode = {
            '0' : '0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111',
            }
arr = ""
for i in file_input:
    arr = i.strip()

# arr = "C200B40A82" # type 0
# arr = "04005AC33890" # type 1
# arr = "880086C3E88112" # type 2
# arr = "CE00C43D881120" # type 3
# arr = "D8005AC2A8F0" # type 6
# arr = "F600BC2D8F" # type 5
# arr = "9C005AC2F8F0" # type 7
# arr = "9C0141080250320F1802104A08" # type 7 ( here nested type 0 = type 1)

coded = ""
for _ in arr:
    coded+=decode[_]
# print(arr)
# print(coded)

file_input.close()
summ_versions = 0

def binarytodecimal(n):
    return int(n, 2)

def make_dic():
    d = {
           # -1 : [],
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            4 : [],
            5 : [],
            6 : [],
            7 : []
            }
    return d

# def operate(ID, ttype):
#     arr = ttype[ID]
#     if ID == 0:
#         summ = 0
#         for i in arr:
#             summ += i
#         return summ
#     elif ID == 1:
#         prod = 1
#         for i in arr:
#             prod*=i
#         return prod
#     elif ID == 2:
#         return min(arr)
#     elif ID == 3:
#         return max(arr)
#     elif ID == 5:
#         res = 0
#         if arr[0] > arr[1]:
#             res = 1
#         return res
#     elif ID == 6:
#         res = 1
#         if arr[0] > arr[1]:
#             res = 0
#         return res
#     elif ID == 7:
#         res = 0
#         if arr[0] == arr[1]:
#             res = 1
#         return res

def operate2(ID, arr):
    # arr = ttype[ID]
    if ID == 0:
        summ = 0
        for i in arr:
            summ += i
        return summ
    elif ID == 1:
        prod = 1
        for i in arr:
            prod*=i
        return prod
    elif ID == 2:
        return min(arr)
    elif ID == 3:
        return max(arr)
    elif ID == 5:
        res = 0
        if arr[0] > arr[1]:
            res = 1
        return res
    elif ID == 6:
        res = 1
        if arr[0] > arr[1]:
            res = 0
        return res
    elif ID == 7:
        res = 0
        if arr[0] == arr[1]:
            res = 1
        return res


message = ""

# def decode(coded, i, v_summ):
def decode(coded, i, dic_type):
    # print(len(coded))
    VVV = coded[i:i+3]
    i = i+3
    TTT = coded[i:i+3]
    i = i+3
    # print("vesrion", VVV, binarytodecimal(VVV))
    # v_summ += binarytodecimal(VVV)
    type_TTT = binarytodecimal(TTT)
    # if binarytodecimal(TTT) == 4:
    #     type_TTT = t
    # else:
    #     type_TTT = t

    # print("Type -", TTT, binarytodecimal(TTT))
    if binarytodecimal(TTT) == 4:
        coding_type = "literal"
    else:
        coding_type = "operator"
    # print(coding_type)

    message = ""
    mess = []
    # last_zero_length = 0
    # dic_type = make_dic()

    
    if coding_type == "literal":
        j = 0
        count = 0
        while True:
            count += 1
            m = coded[i:i+5]
            mess.append(m)            
            i = i+5
            j += 1
            # print(m)
            # print(m[0:1])
            # input()
            if m[0:1] == '0':
                break
        # last_zero_length = 6 + (count*5)
        toprocess = "".join([n[1:] for n in mess])
        # print(toprocess, i, last_zero_length)
        message = binarytodecimal(toprocess)
        # print("d -", dic_type)
        
        # if type_TTT in dic_type:
        #         dic_type[type_TTT].append(binarytodecimal(toprocess))
        # else :
        #     dic_type[type_TTT] = [binarytodecimal(toprocess)]
        
        # dic_type[type_TTT].append(binarytodecimal(toprocess))
        # b_arr.append(binarytodecimal(toprocess))
        
        # print("- ", binarytodecimal(toprocess))
        # a = operate(type_TTT, dic_type)
        # dic_type[type_TTT] = [a]
        # print("in literal", dic_type)
        return i, message
        # return (i, v_summ)

    elif coding_type == "operator":
        # type_TTT = 
        dic_type = []

        typeID = coded[i:i+1]
        i = i+1

        if typeID == "0":
            # print("type ID", typeID)
            pack_length = binarytodecimal(coded[i:i+15])
            # print("Pack lenght :", pack_length)
            i = i+15
            inner_pack_len = i + pack_length
            while i < inner_pack_len:
                # print(coded[i:])
                res = decode(coded[i:], 0, dic_type)
                len_packet = res[0]
                a = res[1]
                dic_type.append(a)

        
                # dic_type[type_TTT].append(res[3])
                # v_summ = res[1]
                # dic_type = res[3]
                # dic_type = copy_dic(res[1], dic_type)
                # len_packet = decode(coded[i:], 0)
                # print(binarytodecimal(coded[i:i+len_packet]))
                i = i + len_packet
            # i = (inner_pack_len)
            # print("in op 0 ", res[1])
            # a = operate(type_TTT , res[1])
            # r_Arr.append(operate2(type_TTT, b_arr))
            return i, operate2(type_TTT, dic_type)

            # print("r\t :",a)
            # # dic_type = make_dic()
            # dic_type[t].append(a)

        elif typeID == "1":
            # print("type ID", typeID)
            no_packs = binarytodecimal(coded[i:i+11])
            # print("iterations : ", no_packs)
            i = i+11
            count = 0
            len_packet = 0
            
            while count < no_packs:
                # print(coded[i:])
                res = decode(coded[i:], 0, dic_type)
                len_packet = res[0]
                # print(res[3])
                # dic_type[type_TTT].append(res[3])
                # v_summ = res[1]
                # dic_type = res[3]
                # dic_type = copy_dic(res[1], dic_type)
                a = res[1]
                dic_type.append(a)
                i = i + len_packet
                count +=1
            # print("in op 1 :", res[1])
            # a = operate(type_TTT , res[1])
            # dic_type = make_dic()
            # r_Arr.append(operate2(type_TTT, b_arr))

            # dic_type[t].append(a)
            # print("in op 1 :", dic_type)
            return i, operate2(type_TTT, dic_type)

    #     print("r\t:", a)
    #     dic_type[t].append(a)
    #     b_arr.append(a)
    # print(b_arr)
    # return (i, dic_type, type_TTT, a)
        # return (i, v_summ)
        

di = []
# message = "".join(map(str, toprocess))
res = decode(coded, 0, di)

# a = operate(ty , res[1])
# print("r\t:", a)
print(res)
# print("s:",sum(b_arr))
# print(r_Arr)
# decode(coded, 0)
# print(message, summ_versions)
        