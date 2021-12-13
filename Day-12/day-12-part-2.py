# file_input = open("day-12-input.txt", "r")

file_input = open("day-12-test.txt", "r")
# file_input = open("day-12-test-2.txt", "r")
# file_input = open("day-12-test-3.txt", "r")
#a = tuple(file_input.readline().strip().split("-"))
#print(a)
# edge = []
dict_net = {}
small = []
# large = []
# travelled = []
# temp = []


def make_possible_paths_list(paths):
    pt1, pt2 = paths[0], paths[1]
    if pt1.islower() and pt1 not in small:
        small.append(pt1)
    if pt2.islower() and pt2 not in small:
        small.append(pt2)

    if pt1 == 'start' or pt2 == 'end':
        # edge.append(tuple([pt1, pt2]))
        if pt1 in dict_net:
            dict_net[pt1].append(pt2)
        else :
            dict_net[pt1] = [pt2]
    elif pt2 == 'start' or pt1 == 'end':
        # edge.append(tuple([pt2, pt1]))
        if pt2 in dict_net:
            dict_net[pt2].append(pt1)
        else :
            dict_net[pt2] = [pt1]
    else:
        # edge.append(tuple([pt1, pt2]))
        # edge.append(tuple([pt2, pt1]))
        if pt1 in dict_net:
            dict_net[pt1].append(pt2)
        else :
            dict_net[pt1] = [pt2]
        if pt2 in dict_net:
            dict_net[pt2].append(pt1)
        else :
            dict_net[pt2] = [pt1]


for i in file_input:
    a = i.strip().split("-")
    make_possible_paths_list(a)
# print(edge)
# print(dict_net)
# print(small)
file_input.close()

starter = []
travelled_All = []

# small_visited = {}
# s_visited = []
# count = 0
# def occurance(no, t_his):
#     occ = {}
#     a = 0
#     for i in t_his:
#         if i in small:
#             if i not in occ:
#                 occ[i] = 0
#             else:
#                 occ[i]+=1
#     if no in list(occ.keys()):
#         a = occ[no]
#     return a

def find_next(at, _travelled):
    
    # t = travelled
    travelled = [_ for _ in _travelled]
    if at == "end":
        z = [_ for _ in travelled]
        travelled_All.append(z)
        print(travelled)
        # return True
    elif at in dict_net:
        # travelled = ["start"]
        next_possible = dict_net[at]
        for i in next_possible: 
            travelled = [_ for _ in _travelled]
            # print("= = =",travelled)
            # print("-----", [travelled.count(j)>1 for j in travelled if j.islower()])
            if i in travelled and i in small and any(travelled.count(j)>1 for j in travelled if j.islower()):
                #if occurance(i, list(small_visited.keys())) > 1:
                    continue

            travelled.append(i)
            t = [_ for _ in travelled]
            find_next(i, t)
            
    else : 
        print("error")


for _ in dict_net["start"]:
    print(_)
    # travelled = ["start", _]
    starter = ["start", _]
    find_next(_, starter)
# find_next("start", ["start"])
# print(travelled)
print(len(travelled_All))