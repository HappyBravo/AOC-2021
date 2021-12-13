import time
#file_input = open("day-6-input.txt", "r")
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

file_input = open("day-6-test.txt", "r")
# f = open('puzzle6.input')
arr = [int(x) for x in file_input.readline().split(',')]
agegroup = [0]*9 ## 0-8 days old
for f in arr: agegroup[f] += 1
days = int(input("Enter days for production : "))
# days = 256
for d in range(days):
    # print(animation[idx % len(animation)], end="\r")
    idx += 1
    # time.sleep(0.05)
    agegroup[(d+7)%9] += agegroup[d%9]
    # print("Day {}\t : {}".format(idx, agegroup))
    print("Day {}\t : {}".format(idx, sum(agegroup)))

print("Result :",sum(agegroup))