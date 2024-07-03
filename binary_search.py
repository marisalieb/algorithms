# implementation of the binary search algorithm
# proving that naive search is slower that binary search
# naive search: scan list asking if it is equal to target
# if yes return inex, if no, return -1

def naive_search(list1, target):  # giving it a list and a target
    for index in range(len(list1)):  # so for every index in list
        if list1[index] == target:  # if list1 at that index then return index
            return index
        return -1  # otherwise we have gone through the entire list and it is not there


# binary search is a bit like divide and conquer, uses the fact that the list is sorted
def binary_search(list1, target):
    # first find midpoint to divide at
    midpoint = len(list1) // 2

    if list1[midpoint] == target:  #list1's index is at the midpoint
        return midpoint

    elif target < list1[midpoint]:
        return binary_search




list1 = [1, 3, 5, 7, 9, 11, 13, 345, 2341]
print((len(list1)))


