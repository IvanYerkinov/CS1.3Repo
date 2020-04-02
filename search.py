
def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:
        return index

    if index == len(array):
        return None
    else:
        return linear_search_recursive(array, item, index+1)
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    start, size = 0, (len(array) - 1)

    while start <= size:
        middle = (start + size)//2
        if array[middle] == item:
            return middle
        if array[size] < item:
            size = middle - 1
        else:
            start = middle + 1
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if right is None:
        right = len(array) - 1
    if left > right:
        return None

    middle = (left + right) // 2
    if item == array[middle]:
        return middle
    if item < array[middle]:
        return binary_search_recursive(array, item, left, middle-1)
    return binary_search_recursive(array, item, middle+1, right)

    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
