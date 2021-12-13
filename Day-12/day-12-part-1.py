# file_input = open("day-12-input.txt", "r")
# from os import path, stat_result


file_input = open("day-12-test.txt", "r")
# file_input = open("day-12-test-2.txt", "r")
# file_input = open("day-12-test-3.txt", "r")
#a = tuple(file_input.readline().strip().split("-"))
#print(a)
edge = []
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
        edge.append(tuple([pt1, pt2]))
        if pt1 in dict_net:
            dict_net[pt1].append(pt2)
        else :
            dict_net[pt1] = [pt2]
    elif pt2 == 'start' or pt1 == 'end':
        edge.append(tuple([pt2, pt1]))
        if pt2 in dict_net:
            dict_net[pt2].append(pt1)
        else :
            dict_net[pt2] = [pt1]
    else:
        edge.append(tuple([pt1, pt2]))
        edge.append(tuple([pt2, pt1]))
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
print(dict_net)
print(small)
file_input.close()
# all_path = []
# count = 0
# temp = []
# def find_next(at, path_ended, prev_trav):
#     next_possible = []
#     # print(temp)
#     if at in dict_net:
#         next_possible = dict_net[at]
#         for _ in next_possible:
#             if _ in prev_trav and _ in small:
#                 continue
#             prev_trav.append(_)
#             if _ == 'end':
#                 # travelled.append(_)
#                 # temp = []
#                 travelled.append(prev_trav)
#                 # print(travelled)
#                 prev_trav = []
#                 return
#                 # all_path.append(travelled)
#                 # path_ended = True
#                 # return path_ended
#             # else :
#             find_next(_, path_ended, prev_trav)
#                 # print(travelled)
#                 # path_ended = False
#                 # return path_ended
#     # else:
#     #     return
starter = []
travelled_All = []
# travelled = []

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
        next_possible = dict_net[at] # [_ for _ in dict_net[at]]
        # n = []
        for i in next_possible: 
            travelled = [_ for _ in _travelled]

            if i in travelled and i in small:
                continue
            # n.append(i)
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