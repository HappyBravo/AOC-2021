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
for i in file_input:
    arr = i.strip()
coded = ""
for _ in arr:
    coded+=decode[_]
print(arr)
print(coded)
file_input.close()
summ_versions = 0

def binarytodecimal(n):
    return int(n, 2)

message = ""

def decode(coded, i, v_summ):
    print(len(coded))
    VVV = coded[i:i+3]
    i = i+3
    TTT = coded[i:i+3]
    i = i+3
    print("vesrion", VVV, binarytodecimal(VVV))
    v_summ += binarytodecimal(VVV)
    print("Type -", TTT, binarytodecimal(TTT))
    if binarytodecimal(TTT) == 4:
        coding_type = "literal"
    else:
        coding_type = "operator"
    print(coding_type)
    message = ""
    mess = []
    last_zero_length = 0
    if coding_type == "literal":
        j = 0
        count = 0
        while True:
            count += 1
            m = coded[i:i+5]
            mess.append(m)            
            i = i+5
            j += 1
            print(m)
            # print(m[0:1])
            # input()
            if m[0:1] == '0':
                break
        last_zero_length = 6 + (count*5)
        toprocess = "".join([n[1:] for n in mess])
        print(toprocess, i, last_zero_length)
        # message = binarytodecimal(toprocess)
        print("- ", binarytodecimal(toprocess))
        return (i, v_summ)
    elif coding_type == "operator":
        typeID = coded[i:i+1]
        i = i+1
        if typeID == "0":
            print("type ID", typeID)
            pack_length = binarytodecimal(coded[i:i+15])
            print("Pack lenght :", pack_length)
            i = i+15
            inner_pack_len = i + pack_length
            while i < inner_pack_len:
                print(coded[i:])
                res = decode(coded[i:], 0, v_summ)
                len_packet = res[0]
                v_summ = res[1]
                # len_packet = decode(coded[i:], 0)
                # print(binarytodecimal(coded[i:i+len_packet]))
                i = i + len_packet
            i = (inner_pack_len)
        elif typeID == "1":
            print("type ID", typeID)

            no_packs = binarytodecimal(coded[i:i+11])
            print("iterations : ", no_packs)
            i = i+11
            count = 0
            len_packet = 0
            while count < no_packs:
                print(coded[i:])
                res = decode(coded[i:], 0, v_summ)
                len_packet = res[0]
                v_summ = res[1]
                i = i + len_packet
                count +=1
        return (i, v_summ)


# message = "".join(map(str, toprocess))
res = decode(coded, 0, summ_versions)
len_packet = res[0]
summ_versions += res[1]
# decode(coded, 0)
print(message, summ_versions)
        