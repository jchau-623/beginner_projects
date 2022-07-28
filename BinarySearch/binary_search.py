#scans entire list and ask if its equal to target
# if yes, return i
#if no, return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target):
