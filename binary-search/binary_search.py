# implementation of the binary search algorithm
import random
import time

def naive_search(any_list, target):  # giving it a list and a target
    for index in range(len(any_list)):  # so for every index in list
        if any_list[index] == target:  # if target at that index then return index
            return index
    return -1  # otherwise we have gone through the entire list and it is not there

def binary_search(any_list, target, low=None, high=None):  #add low and high so lowest and highest indexes you search
    if low is None:
        low = 0
    if high is None:
        high = len(any_list) - 1  # - 1 since len is length and were looking for index

    if high < low:  # should only happen when target is not in list
        return -1

    #change midpoint from len of list to low + high for recursion
    midpoint = (low + high) // 2  # // means divided by 2 with rest

    if any_list[midpoint] == target:
        return midpoint

    elif target < any_list[midpoint]:
        return binary_search(any_list, target, low, midpoint-1)  # is any list for now change later to divide

    else:
        # target > any_list[midpoint]
        return binary_search(any_list, target, midpoint+1, high)


if __name__ == '__main__':

    list1 = [1, 3, 5, 7, 9, 11, 13, 345, 2341]
    target = 11

    print(naive_search(list1, target))
    print(binary_search(list1, target))


    # TIMING

    # build a sorted list of 10000 items
    length = 100
    sorted_list = set()  # so first unordered
    while len(sorted_list) < length:  #  add items until you have 10000
        sorted_list.add(random.randint(-5*length, 5*length))  # range of length*10 to add from

    # make the random list that's still a set into a list and then sort it
    sorted_list = sorted(list(sorted_list))

    start = time.time()  # so thats the time right now
    for target in sorted_list:
        naive_search(sorted_list, target)  # go through whole list and make everything the target
                                            # so basically run naive search 10000
    end = time.time()
    print('Naive search time: ', (end - start)/length, ' seconds')  # so per iteration or for each iteration on average

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
        # so basically run naive search 10000
    end = time.time()
    print('Naive search time: ', (end - start) / length, ' seconds')


    # random target
    target = random.choice(sorted_list)
    print('Binary search index:', binary_search(sorted_list, target), ', Target:', target)
    print('Naive search index:', naive_search(sorted_list, target), ', Target:', target)
