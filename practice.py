def sum_elements(elems):
    """
    list(int) -> int
    sum all elements in list
    """
    sum = 0
    for elem in elems:
        sum += elem

    return sum

def multiply_elements(elems):
    """
    list(int) -> int
    multiply all elements in list
    """
    sum = 1
    for elem in elems:
        sum *= elem

    return sum

def largest_num(elems):
    """
    list(int) -> int
    return largest number in list
    """
    maxNum = 0

    for elem in elems:
        maxNum = max(elem,maxNum)

    return maxNum

def smallest_num(elems):
    """
    list(int) -> int
    return smallest number in list
    """
    minNum = 0

    for elem in elems:
        minNum = min(elem,minNum)

    return minNum

