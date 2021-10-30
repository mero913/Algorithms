# Binary search - by analogy with "phonebook"

def binary_search(list, item):

    low = 0
    high = len(list) - 1

    while low<=high:
        mid = (high + low)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
my_item = 5

print(binary_search(my_list, my_item))
                                                                                                                                                          