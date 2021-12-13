import time

# animation = "|/-\\"
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]
idx = 0
    # while thing_not_complete():
    #     print(animation[idx % len(animation)], end="\r")
    #     idx += 1
    #     time.sleep(0.1)

file_input = open("day-6-input.txt", "r")
# file_input = open("day-6-test.txt", "r")
arr = list(map(int, file_input.readline().split(",")))
# print(arr)
# print(type(arr[0]))
file_input.close()

def fish_update(init_arr, max_days):
    day_count = 0
    idx = 0
    while True:
        idx = 0
        # print(day_count)
        if day_count>=max_days:
            return init_arr
        else:
            for i in range(len(init_arr)):
                # - - - - - - - 
                # print(animation[idx % len(animation)], end="\r")
                # idx += 1
                # time.sleep(0.005)
                # - - - - - - - - - 
                no = init_arr[i]
                if no > 0:
                    init_arr[i] -= 1
                elif no == 0:
                    init_arr[i] = 6
                    init_arr.append(8)
        print("Day {} : {}".format(day_count, len(init_arr)))
        
        day_count+=1
final = fish_update(arr, 256)
# print(final)
print(len(final))
            